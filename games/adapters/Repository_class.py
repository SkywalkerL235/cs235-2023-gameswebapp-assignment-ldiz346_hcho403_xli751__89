from games.adapters.repository import AbstractRepository
from games.domainmodel.model import Game, Genre, Publisher, User, Review

class MemoryRepository(AbstractRepository):
    def __init__(self):
        self.games = []  # List to store games
        # Initialize other data structures as needed

    def get_game_by_id(self, game_id: int) -> Game:
        # Implement the logic to retrieve a game by its ID
        pass

    def get_all_games(self) -> list[Game]:
        # Implement the logic to retrieve all games
        pass

    def get_games_by_genre(self, genre: Genre) -> list[Game]:
        # Implement the logic to retrieve games by genre
        pass

    # Implement other methods for adding, updating, and deleting entities