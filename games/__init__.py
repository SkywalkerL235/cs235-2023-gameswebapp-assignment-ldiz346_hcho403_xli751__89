"""Initialize Flask app."""
from flask import Flask, render_template, redirect, url_for, request

import games.adapters.Abstract_class as repo
from games.adapters import database_repository
from games.adapters.Repository_class import MemoryRepository, populate

from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from sqlalchemy.pool import NullPool

from games.adapters.orm import map_model_to_tables, metadata

'''# TODO: Access to the games should be implemented via the repository pattern and using blueprints, so this can not
#  stay here!
def create_some_game():
    some_game = Game(1, "Call of Duty® 4: Modern Warfare®")
    some_game.release_date = "Nov 12, 2007"
    some_game.price = 9.99
    some_game.description = "The new action-thriller from the award-winning team at Infinity Ward, the creators of " \
                            "the Call of Duty® series, delivers the most intense and cinematic action experience ever. "
    some_game.image_url = "https://cdn.akamai.steamstatic.com/steam/apps/7940/header.jpg?t=1646762118"
    return some_game'''
###from games.adapters.repository import MemoryRepository
# Create an instance of the repository
# Inject the repository instance into your application components


def create_app(test_config=None):

    app = Flask(__name__)
    app.config.from_object('config.Config')
    data_path = Path('games') / 'adapters' / 'data'

    if test_config is not None:
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    # When using memory repository...
    if app.config['REPOSITORY'] == 'memory':
        repo.repo_instance = MemoryRepository()
        database_mode = False
        populate(data_path, repo.repo_instance, database_mode)

    # When using database repository...
    elif app.config['REPOSITORY'] == 'database':
        # refer to .env file
        database_uri = app.config['SQLALCHEMY_DATABASE_URI']
        database_echo = app.config['SQLALCHEMY_ECHO']

        # don't change settings for connect_args & poolclass
        database_engine = create_engine(database_uri, connect_args={"check_same_thread": False}, poolclass=NullPool,
                                        echo=database_echo)
        # create session w/ session maker
        session_factory = sessionmaker(autocommit=False, autoflush=True, bind=database_engine)

        # sqlite3-based repository
        repo.repo_instance = database_repository.SqlAlchemyRepository(session_factory)

        # For testing / first-time use of web app
        if app.config['TESTING'] == 'True' or len(database_engine.table_names()) == 0:
            print("REPOPULATING DATABASE...")
            clear_mappers()
            metadata.create_all(database_engine)
            for table in reversed(metadata.sorted_tables):  # Remove any data from the tables.
                database_engine.execute(table.delete())

            # generate mappings
            map_model_to_tables()

            database_mode = True
            populate(data_path, repo.repo_instance, database_mode)
            print("REPOPULATING DATABASE... FINISHED")

        # Just generate mappings
        else:
            map_model_to_tables()

    # Build the application
    with app.app_context():
        # Register blueprints.
        from games.home import home
        from games.search import search
        from games.gameDescription import gameDescription
        from games.all_games import games
        from games.filtered_games import filtered_games
        from games.profile import profile
        from games.Wishlistt import Wishlist
        from games.authentication import authentication
        app.register_blueprint(home.home_blueprint)
        app.register_blueprint(gameDescription.gameDes_blueprint)
        app.register_blueprint(games.games_blueprint)
        app.register_blueprint(search.search_blueprint)
        app.register_blueprint(filtered_games.filtered_blueprint)
        app.register_blueprint(profile.profile_blueprint)
        app.register_blueprint(Wishlist.wishlist_blueprint)
        app.register_blueprint(authentication.authentication_blueprint)

        # Register a callback the makes sure that database sessions are associated with http requests
        # We reset the session inside the database repository before a new flask request is generated
        @app.before_request
        def before_flask_http_request_function():
            if isinstance(repo.repo_instance, database_repository.SqlAlchemyRepository):
                repo.repo_instance.reset_session()

        # Register a tear-down method that will be called after each request has been processed.
        @app.teardown_appcontext
        def shutdown_session(exception=None):
            if isinstance(repo.repo_instance, database_repository.SqlAlchemyRepository):
                repo.repo_instance.close_session()

    return app
