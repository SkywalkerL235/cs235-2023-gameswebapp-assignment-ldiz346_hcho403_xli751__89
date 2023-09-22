from games.adapters.Abstract_class import AbstractRepository


def get_games(repo: AbstractRepository):
    return repo.get_all_games()


def get_unique_genres(repo: AbstractRepository):
    return repo.get_unique_genres()


def get_name_search_list(repo: AbstractRepository, listofgames, target):
    return repo.get_name_search_list(listofgames, target)


def get_publisher_search_list(repo: AbstractRepository, listofgames, target):
    return repo.get_publisher_search_list(listofgames, target)
