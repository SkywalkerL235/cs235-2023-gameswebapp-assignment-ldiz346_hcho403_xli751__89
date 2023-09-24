from flask import Blueprint, render_template, redirect, url_for, flash
import games.adapters.Abstract_class as repo
from games.Wishlistt import services
from flask import session
from games.authentication.authentication import login_required


wishlist_blueprint = Blueprint('wishlist_bp', __name__)

@wishlist_blueprint.route('/wishlist')
@login_required
def show_wishlist():
    wishlist = services.get_wishlist(repo.repo_instance)
    unique_genres = services.get_unique_genres(repo.repo_instance)
    return render_template('profile.html', wishlist=wishlist, unique_genres=unique_genres)


@wishlist_blueprint.route('/wishlist/add/<game_id>', methods=['POST'])
@login_required
def add_to_wishlist(game_id):
    game_id = int(game_id)

    game = services.get_game_by_id(repo.repo_instance,game_id)

    username = session.get('username')

   # if not services.game_in_wishlist(username, repo.repo_instance,game_id):
    services.add_game_to_wishlist(username, repo.repo_instance,game_id)
    flash('Game added to wishlist!', 'success')
    #else:
        #flash('Game already in wishlist!', 'warning')

    return redirect(url_for('gameDes_bp.show_gamedesc', gameToDisplay=game_id))


@wishlist_blueprint.route('/wishlist/remove/<game_id>', methods=['POST'])
def remove_from_wishlist(game_id):
    game_id = int(game_id)
    services.remove_game_from_wishlist(repo.repo_instance, game_id)
    flash('Game removed from wishlist!', 'warning')
    return redirect(url_for('wishlist_bp.show_wishlist'))

