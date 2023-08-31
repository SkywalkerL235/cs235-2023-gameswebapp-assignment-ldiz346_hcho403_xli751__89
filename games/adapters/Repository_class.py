import games.adapters.Abstract_class
from games.domainmodel.model import Game, Genre, Publisher, User, Review

class MemoryRepository(Abstract_class):
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

    def get_unique_genres(self):
        games_file_name = "games/adapters/data/games.csv"
        reader = GameFileCSVReader(games_file_name)
        reader.read_csv_file()
        raw_games_list = reader.dataset_of_games
        unique_genres = set()  # Using a set to ensure uniqueness
        for game in raw_games_list:
            for genre in game.genres:
                unique_genres.add(genre.genre_name)
        return sorted(unique_genres)  # Return a sorted list of unique genres

    def filter_by_genre(self, selected_genre):
        games_file_name = "games/adapters/data/games.csv"
        reader = GameFileCSVReader(games_file_name)
        reader.read_csv_file()
        raw_games_list = reader.dataset_of_games
        listofgames = []

        for game in raw_games_list:
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