from games.adapters.Abstract_class import AbstractRepository


def get_unique_genres(repo: AbstractRepository):
    return repo.get_unique_genres()
