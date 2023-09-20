from flask import Blueprint, render_template,request
from games.adapters.Repository_class import MemoryRepository
repository = MemoryRepository()
search_blueprint = Blueprint(
    'saerch_bp', __name__)
@search_blueprint.route('/n_search', methods = ["POST","GET"])
def show_name_search():
    unique_genres = repository.get_unique_genres()
    listofgames = repository.get_all_games()
    if request.method == "POST":
         target = request.form["search"]
         search_list = repository.get_name_search_list(listofgames,target)
    else:
        target = ""
        search_list = []
    number_of_total_games = len(search_list)
    return render_template('name_search.html', listOfSearches=search_list, target=target,
                            amount_result=number_of_total_games, unique_genres=unique_genres,
                           )

@search_blueprint.route('/p_search', methods=["POST", "GET"])
def show_publisher_search():
    unique_genres = repository.get_unique_genres()
    listofgames = repository.get_all_games()
    if request.method == "POST":
        target = request.form["search"]
        search_list = repository.get_publisher_search_list(listofgames,target)
    else:
        target = ""
        search_list = []
    number_of_total_games = len(search_list)
    return render_template('publisher_search.html', listOfSearches=search_list, target=target,
                           amount_result=number_of_total_games, unique_genres=unique_genres)

@search_blueprint.route('/g_search')
def show_genre_search():
    unique_genres = repository.get_unique_genres()
    return render_template('genre_search.html',unique_genres=unique_genres)