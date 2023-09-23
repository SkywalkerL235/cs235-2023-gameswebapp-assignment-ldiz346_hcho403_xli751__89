'''from flask import Blueprint, render_template, request, redirect, url_for
import games.adapters.Abstract_class as repo
from games.reviewss import services

reviews_blueprint = Blueprint('reviews_bp', __name__)


@reviews_blueprint.route('/reviews', methods=['GET'])
def show_reviews():
    # fetch all reviews
    reviews = services.get_all_reviews(repo.repo_instance)
    return render_template('gameDescription.html', reviews=reviews)


@reviews_blueprint.route('/reviews/add', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        # Logic to add review
        content = request.form['content']
        # More data extraction here if needed
        repo.repo_instance.services.add_review(content)  # Or however you would handle this
        return redirect(url_for('reviews_bp.show_reviews'))
    return render_template('gameDescription.html')


@reviews_blueprint.route('/reviews/edit/<int:review_id>', methods=['GET', 'POST'])
def edit_review(review_id):
    if request.method == 'POST':
        # Logic to edit review
        content = request.form['content']
        services.edit_review(repo.repo_instance, review_id, content)
        return redirect(url_for('reviews_bp.show_reviews'))
    review = services.get_review_by_id(repo.repo_instance, review_id)
    return render_template('gameDescription.html', review=review)


@reviews_blueprint.route('/reviews/delete/<int:review_id>', methods=['POST'])
def delete_review(review_id):
    services.delete_review(repo.repo_instance, review_id)
    return redirect(url_for('reviews_bp.show_reviews'))

# Additional routes and logic for reviews can be added here as necessary
'''
