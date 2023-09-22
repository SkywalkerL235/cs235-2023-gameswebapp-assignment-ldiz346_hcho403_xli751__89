from flask import Blueprint, render_template
import games.adapters.Abstract_class as repo
from games.all_games import services

home_blueprint = Blueprint(
    'home_bp', __name__)


@home_blueprint.route('/')
def show_home():
    unique_genres = services.get_unique_genres(repo.repo_instance)
    return render_template('home/home.html', unique_genres=unique_genres)
