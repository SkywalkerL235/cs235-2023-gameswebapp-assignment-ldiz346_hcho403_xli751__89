
from abc import ABC, abstractmethod
from games.domainmodel.model import Game, Genre, Publisher, User, Review


class AbstractRepository(ABC):
    @abstractmethod
    def get_game_by_id(self, game_id: int) -> Game:
        pass

    @abstractmethod
    def get_all_games(self) -> list[Game]:
        pass

    @abstractmethod
    def add_game(self, game: Game):
        pass

    @abstractmethod
    def get_unique_genres(self) -> list[str]:
        pass

    @abstractmethod
    def filter_by_genre(self, selected_genre: str) -> list[Game]:
        pass