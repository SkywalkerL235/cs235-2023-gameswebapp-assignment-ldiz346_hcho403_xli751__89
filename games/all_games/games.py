from flask import Blueprint,render_template,request
from games.adapters.Repository_class import MemoryRepository
repository = MemoryRepository()

games_blueprint = Blueprint(
    'games_bp', __name__)
@games_blueprint.route('/games')
def show_games():
    page = request.args.get('page', default=1, type=int)  # Get the page number from the query parameter
    per_page = 20
    listofgames = repository.get_all_games()
    number_of_total_games = len(listofgames)

    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    games_subset = listofgames[start_idx:end_idx]

    unique_genres = repository.get_unique_genres()
    return render_template(
            'games.html',
            listOfGames=games_subset,
            unique_genres=unique_genres,
            page=page,
            per_page=per_page,
            total_number_games=number_of_total_games
        )