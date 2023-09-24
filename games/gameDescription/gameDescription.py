from flask import Blueprint, render_template, request, redirect, url_for
import games.adapters.Abstract_class as repo
from games.gameDescription import services

gameDes_blueprint = Blueprint(
    'gameDes_bp', __name__)


@gameDes_blueprint.route('/game/<gameToDisplay>')
def show_gamedesc(gameToDisplay):
    game_id = int(gameToDisplay)
    the_game = services.get_game_description(repo.repo_instance, game_id)
    unique_genres = services.get_unique_genres(repo.repo_instance)
    game_comments = services.get_game_comments(repo.repo_instance, game_id)
    return render_template(
        'gameDescription.html',
        gameToDisplay=the_game,
        unique_genres=unique_genres,
        reviews=game_comments
    )


@gameDes_blueprint.route('/game/<gameToDisplay>', methods=['GET', 'POST'])
def add_review(gameToDisplay):
    game_id = int(gameToDisplay)
    the_game_by_id = services.get_game_by_id(repo.repo_instance, game_id)

    if request.method == 'POST':
        user_rating = int(request.form['rating_form'])
        user_comment = request.form['comment_form']

        services.add_review(repo.repo_instance, the_game_by_id, user_rating, user_comment)  # Or however you would handle this

    the_game = services.get_game_description(repo.repo_instance, game_id)
    unique_genres = services.get_unique_genres(repo.repo_instance)
    game_comments = services.get_game_comments(repo.repo_instance, game_id)

    return render_template(
        'gameDescription.html',
        gameToDisplay=the_game,
        unique_genres=unique_genres,
        reviews=game_comments)
