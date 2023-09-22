from games.adapters.Abstract_class import AbstractRepository


def filter_by_genre(repo: AbstractRepository, selected_genre):
    return repo.filter_by_genre(selected_genre)


def get_unique_genres(repo: AbstractRepository):
    return repo.get_unique_genres()
