"""Initialize Flask app."""
from flask import Flask, render_template, redirect, url_for, request

from games.adapters.Repository_class import MemoryRepository


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

'''unique_genres = repository.get_unique_genres()'''

repository = MemoryRepository()
from games.home import home
from games.search import search
from games.gameDescription import gameDescription
from games.all_games import games
from games.filtered_games import filtered_games


def create_app(repository=repository):


    app = Flask(__name__)

    app.register_blueprint(home.home_blueprint)
    app.register_blueprint(gameDescription.gameDes_blueprint)
    app.register_blueprint(games.games_blueprint)
    app.register_blueprint(search.search_blueprint)
    app.register_blueprint(filtered_games.filtered_blueprint)

    @app.route('/wishlist')
    def show_wishlist():
        unique_genres = repository.get_unique_genres()  # Get unique genres
        return render_template('wishlist.html', unique_genres=unique_genres)

    @app.route('/profile')
    def show_profile():
        unique_genres = repository.get_unique_genres()  # Get unique genres
        return render_template('profile.html', unique_genres=unique_genres)

    @app.route('/login')
    def show_login():
        unique_genres = repository.get_unique_genres()  # Get unique genres
        return render_template('authentication/login.html', unique_genres=unique_genres)

    @app.route('/register')
    def show_register():
        unique_genres = repository.get_unique_genres()  # Get unique genres
        return render_template('authentication/register.html', unique_genres=unique_genres)

    return app




