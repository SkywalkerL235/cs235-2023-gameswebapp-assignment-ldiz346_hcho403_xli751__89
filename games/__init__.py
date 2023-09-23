"""Initialize Flask app."""
from flask import Flask, render_template, redirect, url_for, request
import games.adapters.Abstract_class as repo
from games.adapters.Repository_class import MemoryRepository, populate

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

from games.home import home
from games.search import search
from games.gameDescription import gameDescription
from games.all_games import games
from games.filtered_games import filtered_games
from games.profile import profile
from games.Wishlistt import Wishlist
from games.reviewss import Reviews
from games.authentication import authentication


def create_app():

    app = Flask(__name__)

    repo.repo_instance = MemoryRepository()
    populate(repo.repo_instance)

    app.register_blueprint(home.home_blueprint)
    app.register_blueprint(gameDescription.gameDes_blueprint)
    app.register_blueprint(games.games_blueprint)
    app.register_blueprint(search.search_blueprint)
    app.register_blueprint(filtered_games.filtered_blueprint)
    app.register_blueprint(profile.profile_blueprint)
    app.register_blueprint(Wishlist.wishlist_blueprint)
    app.register_blueprint(Reviews.reviews_blueprint)
    app.register_blueprint(authentication.authentication_blueprint)

    return app
