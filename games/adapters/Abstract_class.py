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
    def get_games_by_genre(self, genre: Genre) -> list[Game]:
        pass