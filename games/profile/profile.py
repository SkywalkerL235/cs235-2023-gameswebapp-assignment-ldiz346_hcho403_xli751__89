from flask import Blueprint, render_template, session, redirect, url_for
import games.adapters.Abstract_class as repo
from games.authentication.authentication import login_required
from games.profile import services


profile_blueprint = Blueprint(
    'profile_bp', __name__)


@profile_blueprint.route('/profile')
@login_required
def show_profile():
    if 'username' not in session:
        return redirect(url_for('authentication_bp.login'))

    username = session['username']
    wishlist = services.get_wishlist(username, repo.repo_instance)

    unique_genres = services.get_unique_genres(repo.repo_instance)
    user_details = services.get_user_details_by_username(session['username'], repo.repo_instance)

    list_to_show = services.get_wishlist_description(repo.repo_instance, wishlist)

    return render_template(
        'profile.html',
        user=user_details,
        wishlist_games=list_to_show,
        unique_genres=unique_genres,
    )