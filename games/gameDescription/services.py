from games.adapters.Abstract_class import AbstractRepository


def get_game_description(repo: AbstractRepository, game_id):
    return repo.get_game_description(game_id)


def get_unique_genres(repo: AbstractRepository):
    return repo.get_unique_genres()
