from flask import Blueprint, render_template
from games.adapters.Repository_class import MemoryRepository
repository = MemoryRepository()

home_blueprint = Blueprint(
    'home_bp', __name__)

@home_blueprint.route('/')
#def home():
        #some_game = create_some_game()
        # Use Jinja to customize a predefined html page rendering the layout for showing a single game.
def show_home():
    unique_genres = repository.get_unique_genres()  # Get unique genres
    return render_template('home/home.html', unique_genres=unique_genres)