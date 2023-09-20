from flask import Blueprint,render_template
from games.adapters.Repository_class import MemoryRepository
repository = MemoryRepository()

gameDes_blueprint = Blueprint(
    'gameDes_bp', __name__)

@gameDes_blueprint.route('/game/<gameToDisplay>')
def show_gamedesc(gameToDisplay):
    game_id = int(gameToDisplay)
    the_game = repository.get_game_description(game_id)
    unique_genres = repository.get_unique_genres()
    return render_template('gameDescription.html', gameToDisplay=the_game, unique_genres=unique_genres)