from flask import Blueprint, render_template, request
import games.adapters.Abstract_class as repo
from games.profile import services

profile_blueprint = Blueprint(
    'profile_bp', __name__)


@profile_blueprint.route('/profile')
def show_profile():
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

    return render_template(
        'profile.html',
        listOfGames=listOfGamesExample
    )
