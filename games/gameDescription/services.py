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


def add_review(repo: AbstractRepository, current_game, user_rating, user_comment):
    example_user = User("HaChoi486", "HelloThere486486")
    repo.add_user(example_user)

    review = Review(example_user, current_game, user_rating, user_comment)
    example_user.add_review(review)
    return repo.add_review(review)


def get_game_comments(repo: AbstractRepository, game_id):
    current_game = repo.get_game_by_id(game_id)
    return repo.get_reviews_by_game(current_game)
