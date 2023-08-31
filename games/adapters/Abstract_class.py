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

    @abstractmethod
    def get_genres(self) -> list[Genre]:
        pass

    @abstractmethod
    def get_publishers(self) -> list[Publisher]:
        pass

    @abstractmethod
    def add_game(self, game: Game):
        pass

    @abstractmethod
    def update_game(self, game: Game):
        pass

    @abstractmethod
    def delete_game(self, game: Game):
        pass

    @abstractmethod
    def add_review(self, game: Game, review: Review):
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def get_users(self) -> list[User]:
        pass

    @abstractmethod
    def add_user(self, user: User):
        pass

    @abstractmethod
    def update_user(self, user: User):
        pass

    @abstractmethod
    def delete_user(self, user: User):
        pass
