from games.adapters.Abstract_class import AbstractRepository


def get_games(repo: AbstractRepository):
    my_list = repo.get_all_games()
    smaller_list = my_list[:3]
    return smaller_list


def get_unique_genres(repo: AbstractRepository):
    return repo.get_unique_genres()
