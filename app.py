from flask import Flask, render_template

from games.domainmodel import model
from games.adapters.datareader import csvdatareader
from games.adapters import data

app = Flask(__name__)

@app.route('/')
def show_layout():
    return render_template('layout.html')

@app.route('/gamesDescription')
def show_gamedesc():
    return render_template('gameDescription.html')

@app.route('/games')
def show_games():
    games_file_name = "static/games.csv"
    reader = csvdatareader.GameFileCSVReader(games_file_name)
    reader.read_csv_file()

    listOfGames = []

    for index in range(0, 10):
        game = reader.dataset_of_games[index]
        Gamepart = f"name': '{game.title}', 'price': '{game.price}', 'image': '{game.image_url}', 'publishers': '{game.publisher}', 'date': '{game.release_date}', 'genres': '{game.genres}', 'reviews': '{len(game.reviews)}'"
        listOfGames.append({Gamepart})


    listOfGamesExample = [{
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
        }]

    return render_template('games.html', listOfGames=listOfGamesExample)

if __name__ == '__app__':
    app.run(debug=True, port=5000)
