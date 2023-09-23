from reviews.adapters.AbstractRepository import AbstractReviewRepository

def get_all_reviews(repo: AbstractReviewRepository):
    return repo.get_all_reviews()

def get_review_by_id(repo: AbstractReviewRepository, review_id):
    return repo.get_review_by_id(review_id)

def add_review(repo: AbstractReviewRepository, content, user_id, game_id):
    review = Review(content=content, user_id=user_id, game_id=game_id)
    return repo.add_review(review)

def edit_review(repo: AbstractReviewRepository, review_id, content):
    return repo.edit_review(review_id, content)

def delete_review(repo: AbstractReviewRepository, review_id):
    return repo.delete_review(review_id)
