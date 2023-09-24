from flask import Blueprint, render_template, session
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

    user_details = services.get_user_details_by_username(session['username'], repo.repo_instance)
    listofgames = services.get_games(repo.repo_instance)
    wishlist = services.get_wishlist_by_username(session['username'], repo.repo_instance)


    return render_template(
        'profile.html',
        user=user_details,
        listOfGames=listofgames,
        wishlist=wishlist
    )
