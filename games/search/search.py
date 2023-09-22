from flask import Blueprint, render_template, request
import games.adapters.Abstract_class as repo
from games.search import services

search_blueprint = Blueprint(
    'saerch_bp', __name__)


@search_blueprint.route('/n_search', methods=["POST", "GET"])
def show_name_search():
    unique_genres = services.get_unique_genres(repo.repo_instance)
    listofgames = services.get_games(repo.repo_instance)
    if request.method == "POST":
        target = request.form["search"]
        search_list = services.get_name_search_list(repo.repo_instance, listofgames, target)
    else:
        target = ""
        search_list = []
    number_of_total_games = len(search_list)
    return render_template(
            'name_search.html',
            listOfSearches=search_list,
            target=target,
            amount_result=number_of_total_games,
            unique_genres=unique_genres,
        )


@search_blueprint.route('/p_search', methods=["POST", "GET"])
def show_publisher_search():
    unique_genres = services.get_unique_genres(repo.repo_instance)
    listofgames = services.get_games(repo.repo_instance)
    if request.method == "POST":
        target = request.form["search"]
        search_list = services.get_publisher_search_list(repo.repo_instance, listofgames, target)
    else:
        target = ""
        search_list = []
    number_of_total_games = len(search_list)
    return render_template(
            'publisher_search.html',
            listOfSearches=search_list,
            target=target,
            amount_result=number_of_total_games,
            unique_genres=unique_genres
        )


@search_blueprint.route('/g_search')
def show_genre_search():
    unique_genres = services.get_unique_genres(repo.repo_instance)
    return render_template(
            'genre_search.html',
            unique_genres=unique_genres
        )
