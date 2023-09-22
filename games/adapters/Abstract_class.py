import abc
from games.domainmodel.model import Game, Genre, Publisher, User, Review

repo_instance = None


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def get_game_by_id(self, game_id: int) -> Game:
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_games(self) -> list[Game]:
        raise NotImplementedError

    @abc.abstractmethod
    def add_game(self, game: Game):
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre_set(self, genre_set):
        raise NotImplementedError

    @abc.abstractmethod
    def add_publisher_set(self, publisher_set):
        raise NotImplementedError

    @abc.abstractmethod
    def get_unique_genres(self) -> list[str]:
        raise NotImplementedError

    @abc.abstractmethod
    def filter_by_genre(self, selected_genre: str) -> list[Game]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_game_description(self, game_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_name_search_list(self, listofgames, target):
        raise NotImplementedError

    @abc.abstractmethod
    def get_publisher_search_list(self, listofgames, target):
        raise NotImplementedError

    @abc.abstractmethod
    def add_user(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, user_name) -> User:
        raise NotImplementedError
