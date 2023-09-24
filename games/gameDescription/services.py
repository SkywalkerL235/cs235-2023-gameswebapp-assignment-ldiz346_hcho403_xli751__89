from games.adapters.Abstract_class import AbstractRepository
from games.domainmodel.model import Review, User


def get_game_description(repo: AbstractRepository, game_id):
    return repo.get_game_description(game_id)


def get_unique_genres(repo: AbstractRepository):
    return repo.get_unique_genres()


def get_all_reviews(repo: AbstractRepository):
    return repo.get_all_reviews()


def get_game_by_id(repo: AbstractRepository, game_id):
    return repo.get_game_by_id(game_id)


def add_review(repo: AbstractRepository, current_game, user_rating, user_comment, user_details):
    review = Review(user_details, current_game, user_rating, user_comment)
    user_details.add_review(review)
    return repo.add_review(review)


def get_game_comments(repo: AbstractRepository, game_id):
    current_game = repo.get_game_by_id(game_id)
    return repo.get_reviews_by_game(current_game)


def get_user_details_by_username(username, repo):
    """
    Fetch user details by a given username from the memory repository.
    """
    user = repo.get_user(username)
    if user:
        # Convert the User object to dictionary or another structure if necessary.
        return user  # Adjust this based on how you're using the user object in your templates.
    raise ValueError("User not found")

def form_comment(comment: Review):
    return None
