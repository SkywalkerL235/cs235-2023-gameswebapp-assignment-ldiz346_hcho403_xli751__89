from flask import Blueprint, render_template, redirect, url_for, flash, session
import games.adapters.Abstract_class as repo
from games.Wishlistt import services
from flask import render_template, request
from games.authentication.authentication import login_required


wishlist_blueprint = Blueprint('wishlist_bp', __name__)

@wishlist_blueprint.route('/wishlist')
@login_required
def show_wishlist():
    username = session['username']
    wishlist = services.get_wishlist_by_username(username, repo.repo_instance)
    unique_genres = services.get_unique_genres(repo.repo_instance)
    user_details = services.get_user_details_by_username(username, repo.repo_instance)

    # Pagination
    page = request.args.get('page', default=1, type=int)  # Get the page number from the query parameter
    per_page = 20  # or any other number you prefer
    number_of_total_games = len(wishlist)  # get the total number of games in the wishlist

    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    wishlist_subset = wishlist[start_idx:end_idx]

    return render_template(
        'wishlist.html',
        wishlist_games=wishlist_subset,
        unique_genres=unique_genres,
        user=user_details,  # sending user details to the template
        page=page,
        per_page=per_page,
        total_number_games=number_of_total_games
    )


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

    return redirect(url_for('wishlist_bp.show_wishlist', gameToDisplay=game_id))


@wishlist_blueprint.route('/wishlist/remove/<game_id>', methods=['POST'])
def remove_from_wishlist(game_id):
    game_id = int(game_id)
    services.remove_game_from_wishlist(repo.repo_instance, game_id)
    flash('Game removed from wishlist!', 'warning')
    return redirect(url_for('wishlist_bp.show_wishlist'))

