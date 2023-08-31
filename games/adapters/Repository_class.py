
from games import GameFileCSVReader
from games.adapters.Abstract_class import AbstractRepository
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

        unique_genres = set()  # Using a set to ensure uniqueness
        for game in self.games:
            for genre in game.genres:
                unique_genres.add(genre.genre_name)
        return sorted(unique_genres)  # Return a sorted list of unique genres

    def filter_by_genre(self, selected_genre):
        listofgames = []

        for game in self.games:
            try:
                list_of_genres = game.genres
                if any(genre.genre_name == selected_genre for genre in list_of_genres):
                    official_genre_string = ', '.join(part.genre_name for part in list_of_genres)

                    if game.price == 0.0:
                        price_string = "Free to play"
                    else:
                        price_string = "$" + str(game.price)

                    Gamepart = {
                        'name': game.title,
                        'price': price_string,
                        'image': game.image_url,
                        'publishers': game.publisher.publisher_name,
                        'date': game.release_date,
                        'genres': official_genre_string,
                        'reviews': len(game.reviews),
                        'id': game.game_id,
                        'about': game.description
                    }
                    listofgames.append(Gamepart)
            except:
                pass
        listofgames.sort(key=lambda x: x['name'])
        return listofgames


    # Implement other methods for adding, updating, and deleting entities
