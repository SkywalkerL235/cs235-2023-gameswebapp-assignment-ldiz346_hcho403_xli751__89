from flask import Blueprint, render_template, request
import games.adapters.Abstract_class as repo
from games.profile import services

profile_blueprint = Blueprint(
    'profile_bp', __name__)


@profile_blueprint.route('/profile')
def show_profile():
    listofgames = services.get_games(repo.repo_instance)
    unique_genres = services.get_unique_genres(repo.repo_instance)
    return render_template(
        'profile.html',
        listOfGames=listofgames,
        unique_genres=unique_genres,
    )
