from flask import Blueprint, render_template, redirect, url_for, flash
import games.adapters.Abstract_class as repo
from games.gameDescription import services as game_services
from games.Wishlistt import services as wishlist_services

wishlist_blueprint = Blueprint('wishlist_bp', __name__)

@wishlist_blueprint.route('/wishlist')
def show_wishlist():
    wishlist = wishlist_services.get_wishlist(repo.repo_instance)
    unique_genres = game_services.get_unique_genres(repo.repo_instance)
    return render_template('wishlist.html', wishlist=wishlist, unique_genres=unique_genres)

@wishlist_blueprint.route('/wishlist/add/<game_id>', methods=['POST'])
def add_to_wishlist(game_id):
    game_id = int(game_id)
    if wishlist_services.game_in_wishlist(repo.repo_instance, game_id) == True:
        wishlist_services.add_game_to_wishlist(repo.repo_instance, game_id)
        flash('Game added to wishlist!', 'success')
    return redirect(url_for('wishlist_bp.show_wishlist'))

@wishlist_blueprint.route('/wishlist/remove/<game_id>', methods=['POST'])
def remove_from_wishlist(game_id):
    game_id = int(game_id)
    wishlist_services.remove_game_from_wishlist(repo.repo_instance, game_id)
    flash('Game removed from wishlist!', 'warning')
    return redirect(url_for('wishlist_bp.show_wishlist'))

