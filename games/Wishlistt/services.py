from games.adapters.Abstract_class import AbstractRepository

#def get_all_games_in_wishlist(repo: AbstractRepository):
   # return repo.get_all_games_in_wishlist()

def add_game_to_wishlist(username, repo: AbstractRepository, game_id: int):
    return repo.add_game_to_wishlist(username, game_id)


def remove_game_from_wishlist(repo: AbstractRepository, game_id: int):
    return repo.remove_game_from_wishlist(game_id)

def game_in_wishlist(repo: AbstractRepository, username: str, game_id: int):
    return repo.game_in_wishlist(username, game_id)


def get_unique_genres(repo: AbstractRepository):
    return repo.get_unique_genres()

def get_game_by_id(repo: AbstractRepository, game_id: int):
    return repo.get_game_by_id(game_id)