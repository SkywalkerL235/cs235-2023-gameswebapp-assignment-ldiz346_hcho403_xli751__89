"""Initialize Flask app."""
from flask import Flask, render_template, redirect, url_for, request

from games.adapters.Repository_class import MemoryRepository


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
        listofgames = repository.get_all_games()
        unique_genres = repository.get_unique_genres()
        return render_template('games.html', listOfGames=listofgames, unique_genres=unique_genres)
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
        return render_template('filtered_games.html', filtered_games=filtered_list, selected_genre=selected_genre, unique_genres=unique_genres)

    return app




