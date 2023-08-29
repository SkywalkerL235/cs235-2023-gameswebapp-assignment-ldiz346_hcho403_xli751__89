"""Initialize Flask app."""
import games.adapters.datareader.csvdatareader
from flask import Flask, render_template, redirect, url_for

from games.adapters.datareader.csvdatareader import GameFileCSVReader
# TODO: Access to the games should be implemented via the repository pattern and using blueprints, so this can not
#  stay here!
from games.domainmodel.model import Game


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


def create_app():
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    @app.route('/')
    #def home():
        #some_game = create_some_game()
        # Use Jinja to customize a predefined html page rendering the layout for showing a single game.
    def show_layout():
        #return render_template('gameDescription.html', game=some_game)
        return render_template('layout.html')

    @app.route('/game/<gameToDisplay>')
    def show_gamedesc(gameToDisplay):
        game_id = int(gameToDisplay)

        games_file_name = "games/adapters/data/games.csv"
        reader = GameFileCSVReader(games_file_name)
        reader.read_csv_file()
        raw_games_list = reader.dataset_of_games

        the_game = None

        for game in raw_games_list:
            if game.game_id == game_id:
                list_of_genres = game.genres
                official_genre_string = ', '.join(part.genre_name for part in list_of_genres)

                if game.price == 0.0:
                    price_string = "Free to play"
                else:
                    price_string = "$" + str(game.price)

                the_game = {
                    'name': game.title,
                    'price': price_string,
                    'image': game.image_url,
                    'publishers': game.publisher.publisher_name,
                    'date': game.release_date,
                    'genres': official_genre_string,
                    'reviews': len(game.reviews),
                    'id': game.game_id,
                    'about': game.description
                }
                break

        return render_template('gameDescription.html', gameToDisplay=the_game)

    @app.route('/games')
    def show_games():
        games_file_name = "games/adapters/data/games.csv"
        reader = GameFileCSVReader(games_file_name)
        reader.read_csv_file()
        raw_games_list = reader.dataset_of_games
        listOfGames = []

        for index in range(0, (len(raw_games_list))):
            game = raw_games_list[index]
            try:
                list_of_genres = game.genres
                official_genre_string = ', '.join(part.genre_name for part in list_of_genres)

                if game.price == 0.0:
                    price_string = "Free to play"
                else:
                    price_string = "$" + str(game.price)

                Gamepart = {
                    'name': game.title,
                    'price': price_string,
                    'image': game.image_url,
                    'publishers': game.publisher.publisher_name,
                    'date': game.release_date,
                    'genres': official_genre_string,
                    'reviews': len(game.reviews),
                    'id': game.game_id,
                    'about': game.description
                }
                listOfGames.append(Gamepart)
            except:
                pass

        '''listOfGamesExample = [{
            'name': 'Oxygen Not Included',
            'price': '$24.99',
            'image': "https://cdn.akamai.steamstatic.com/steam/apps/457140/header_alt_assets_6.jpg?t=1654189805",
            'publishers': 'Klei Entertainment',
            'date': 'Jul 30, 2019',
            'genres': 'Indie,Simulation',
            'reviews': '0'
        },
            {
                'name': 'Sally Face - Episode One',
                'price': '$2.99',
                'image': "https://cdn.akamai.steamstatic.com/steam/apps/541570/header.jpg?t=1619036403",
                'publishers': 'Portable Moose',
                'date': 'Dec 14, 2016',
                'genres': 'Adventure,Indie',
                'reviews': '5'
            },
            {
                'name': 'Super Meat Boy',
                'price': '$14.99',
                'image': "https://cdn.akamai.steamstatic.com/steam/apps/40800/header.jpg?t=1638306971",
                'publishers': 'Unknown',
                'date': 'Nov 30, 2010',
                'genres': 'Indie',
                'reviews': '0'
            }]'''

        return render_template('games.html', listOfGames=listOfGames)

    return app
