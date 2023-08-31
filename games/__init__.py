"""Initialize Flask app."""
from flask import Flask, render_template, redirect, url_for, request

from games.adapters.Repository_class import MemoryRepository


repository = MemoryRepository()
def create_app(repository=repository):


    app = Flask(__name__)

    @app.route('/')
    #def home():
        #some_game = create_some_game()
        # Use Jinja to customize a predefined html page rendering the layout for showing a single game.
    def show_layout():
        unique_genres = repository.get_unique_genres()  # Get unique genres
        return render_template('layout.html', unique_genres=unique_genres)

    @app.route('/game/<gameToDisplay>')
    def show_gamedesc(gameToDisplay):
        game_id = int(gameToDisplay)
        the_game = repository.get_game_description(game_id)

        unique_genres = repository.get_unique_genres()

        return render_template('gameDescription.html', gameToDisplay=the_game, unique_genres=unique_genres)

    @app.route('/games')
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

    @app.route('/N_search', methods = ["POST","GET"])
    def show_name_search():
        unique_genres = repository.get_unique_genres()
        if request.method == "POST":
            target = request.form["search"]
            search_list = repository.get_name_search_list(target)
            return render_template('search.html', listOfSearches = search_list, target = target, amount_result = len(search_list), unique_genres=unique_genres)
        else:
            return render_template('search.html', listOfSearches = [], target = "", amount_result = 0, unique_genres=unique_genres)

    @app.route('/P_search', methods=["POST", "GET"])
    def show_publisher_search():
        unique_genres = repository.get_unique_genres()
        if request.method == "POST":
            target = request.form["search"]
            search_list = repository.get_publisher_search_list(target)
            return render_template('search.html', listOfSearches = search_list, target = target, amount_result = len(search_list), unique_genres=unique_genres)
        else:
            return render_template('search.html', listOfSearches = [], target = "", amount_result = 0, unique_genres=unique_genres)


    @app.route('/filtered_games/<selected_genre>')
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

    return app




