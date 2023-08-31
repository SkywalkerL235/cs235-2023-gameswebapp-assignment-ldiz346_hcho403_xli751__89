
from games.adapters.datareader.csvdatareader import GameFileCSVReader
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
        for items in self.games:
            if items.game_id == game_id:
                return items
        pass

    def get_all_games(self) -> list[Game]:
        listofgames = []

        for game in self.games:
            try:
                list_of_genres = game.genres
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

    def add_game(self, game: Game):
        if game not in self.games:
            self.games.append(game)

    def get_unique_genres(self) -> list[str]:
        unique_genres = set()
        for game in self.games:
            for genre in game.genres:
                unique_genres.add(genre.genre_name)
        return sorted(unique_genres)

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

    def get_game_description(self, game_id):
        the_game = None
        for game in self.games:
            if game.game_id == game_id:
                list_of_genres = game.genres
                official_genre_string = ', '.join(part.genre_name for part in list_of_genres)

                if game.price == 0.0:
                    price_string = "Free to play"
                else:
                    price_string = "$" + str(game.price)

                the_game = {
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
                break
        return the_game

    def get_name_search_list(self, target):
        listofgames = []
        for game in self.games:
            try:
                list_of_genres = game.genres
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
        search_list = []
        if target != '':
            for game in listofgames:
                if target.lower() in game['name'].lower():
                    search_list.append(game)
        search_list.sort(key=lambda x: x['name'])
        return search_list

    def get_publisher_search_list(self,target):
        listofgames = []
        for game in self.games:
            try:
                list_of_genres = game.genres
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
        search_list = []
        if target != '':
            for game in listofgames:
                if target.lower() in game['publishers'].lower():
                    search_list.append(game)
        search_list.sort(key=lambda x: x['publishers'])
        return search_list
    # Implement other methods for adding, updating, and deleting entities
