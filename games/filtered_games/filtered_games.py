from flask import Blueprint,render_template,request
from games.adapters.Repository_class import MemoryRepository
repository = MemoryRepository()

filtered_blueprint = Blueprint(
    'filtered_bp', __name__)

@filtered_blueprint.route('/filtered_games/<selected_genre>')
def filter_by_genre(selected_genre):
    filtered_list = repository.filter_by_genre(selected_genre)
    unique_genres = repository.get_unique_genres()
    page = request.args.get('page', default=1, type=int)  # Get the page number from the query parameter
    per_page = 20
    number_of_total_games = len(filtered_list)

    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    games_subset = filtered_list[start_idx:end_idx]
    return render_template('filtered_games.html', filtered_games=games_subset, selected_genre=selected_genre, unique_genres=unique_genres, page=page,
            per_page=per_page,
            total_number_games=number_of_total_games
        )