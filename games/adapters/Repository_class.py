
from games import GameFileCSVReader
from games.domainmodel.model import Game, Genre, Publisher, User, Review

class MemoryRepository(AbstractRepository):
    def __init__(self):
        self.games = list()
        self.genres = list()
        self.publishers = list()

        games_file_name = "games/adapters/data/games.csv"
        reader = GameFileCSVReader(games_file_name)
        reader.read_csv_file()
        self.games = reader.dataset_of_games
        self.genres = reader.dataset_of_genres
        self.publishers = reader.dataset_of_publishers

    def get_game_by_id(self, game_id: int) -> Game:
        # Implement the logic to retrieve a game by its ID
        pass

    def get_all_games(self) -> list[Game]:
        return self.games

    def get_games_by_genre(self, genre: Genre) -> list[Game]:
        # Implement the logic to retrieve games by genre
        pass

    def get_unique_genres(self):
        return self.genres
