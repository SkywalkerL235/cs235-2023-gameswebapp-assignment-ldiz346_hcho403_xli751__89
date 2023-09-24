from flask import Blueprint, render_template, redirect, url_for, flash
import games.adapters.Abstract_class as repo
from games.Wishlistt import services as wishlist_services
from flask import session
from games.adapters.Repository_class import MemoryRepository
from games.authentication.authentication import login_required

repo_instance = MemoryRepository()


wishlist_blueprint = Blueprint('wishlist_bp', __name__)

@wishlist_blueprint.route('/wishlist')
@login_required
def show_wishlist():
    wishlist = wishlist_services.get_wishlist(repo.repo_instance)
    unique_genres = wishlist_services.get_unique_genres(repo.repo_instance)
    return render_template('profile.html', wishlist=wishlist)


@wishlist_blueprint.route('/wishlist/add/<game_id>', methods=['POST'])
def add_to_wishlist(game_id):
    game_id = int(game_id)

    # Retrieve the game object from the repository
    game = repo.repo_instance.get_game_by_id(game_id)


    # Get the username of the currently logged-in user (modify this based on your implementation)
    username = session.get('username')  # or another mechanism to get the current user's name
    if 'username' not in session:
        next_url = url_for('gameDes_bp.show_gamedesc', gameToDisplay=game_id)
        login_url = url_for('authentication_bp.login', next=next_url)
        return redirect(login_url)

    # Check if the game is already in the wishlist
    if not repo.repo_instance.game_in_wishlist(username, game):

        repo.add_game_to_wishlist(username, game)
        flash('Game added to wishlist!', 'success')
    else:
        flash('Game already in wishlist!', 'warning')

    return redirect(url_for('wishlist_bp.show_wishlist'))


@wishlist_blueprint.route('/wishlist/remove/<game_id>', methods=['POST'])
def remove_from_wishlist(game_id):
    game_id = int(game_id)
    wishlist_services.remove_game_from_wishlist(repo.repo_instance, game_id)
    flash('Game removed from wishlist!', 'warning')
    return redirect(url_for('wishlist_bp.show_wishlist'))

