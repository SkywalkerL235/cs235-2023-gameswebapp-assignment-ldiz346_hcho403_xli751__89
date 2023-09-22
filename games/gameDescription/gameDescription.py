from flask import Blueprint,render_template
import games.adapters.Abstract_class as repo
from games.gameDescription import services

gameDes_blueprint = Blueprint(
    'gameDes_bp', __name__)

@gameDes_blueprint.route('/game/<gameToDisplay>')
def show_gamedesc(gameToDisplay):
    game_id = int(gameToDisplay)
    the_game = services.get_game_description(repo.repo_instance, game_id)
    unique_genres = services.get_unique_genres(repo.repo_instance)
    return render_template(
        'gameDescription.html',
        gameToDisplay=the_game,
        unique_genres=unique_genres)
