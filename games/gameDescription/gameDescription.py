from flask import Blueprint, render_template, request, redirect, url_for, session
import games.adapters.Abstract_class as repo
from games.authentication.authentication import login_required
from games.gameDescription import services

gameDes_blueprint = Blueprint(
    'gameDes_bp', __name__)


@gameDes_blueprint.route('/game/<gameToDisplay>')
def show_gamedesc(gameToDisplay):
    game_id = int(gameToDisplay)
    the_game = services.get_game_description(repo.repo_instance, game_id)
    unique_genres = services.get_unique_genres(repo.repo_instance)
    game_comments = services.get_game_comments(repo.repo_instance, game_id)

    review_list = []

    for comment in game_comments:
        current = services.form_review(repo.repo_instance, comment)
        review_list.append(current)

    return render_template(
        'gameDescription.html',
        gameToDisplay=the_game,
        unique_genres=unique_genres,
        reviews=review_list
    )


@gameDes_blueprint.route('/game/<gameToDisplay>', methods=['GET', 'POST'])
@login_required
def add_review(gameToDisplay):
    game_id = int(gameToDisplay)
    the_game_by_id = services.get_game_by_id(repo.repo_instance, game_id)

    user_details = services.get_user_details_by_username(session['username'], repo.repo_instance)

    if request.method == 'POST':
        user_rating = int(request.form['rating_form'])
        user_comment = request.form['comment_form']

        services.add_review(repo.repo_instance, the_game_by_id, user_rating, user_comment, user_details)  # Or however you would handle this

    if 'username' not in session:
        return redirect(url_for('authentication_bp.login'))

    the_game = services.get_game_description(repo.repo_instance, game_id)
    unique_genres = services.get_unique_genres(repo.repo_instance)
    game_comments = services.get_game_comments(repo.repo_instance, game_id)

    review_list = []

    for comment in game_comments:
        current = services.form_review(repo.repo_instance, comment)
        review_list.append(current)

    return render_template(
        'gameDescription.html',
        gameToDisplay=the_game,
        unique_genres=unique_genres,
        reviews=review_list)
