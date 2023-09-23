
from games.adapters.datareader.csvdatareader import GameFileCSVReader
from games.adapters.Abstract_class import AbstractRepository
from games.domainmodel.model import Game, Genre, Publisher, User, Review, Wishlist

import os

class MemoryRepository(AbstractRepository):
    def __init__(self):
        self.games = list()
        self.genres = list()
        self.publishers = list()
        self.users = list()
        self._wishlists = {}
        self.user_wishlist = {}
        self._reviews = list()

        # games_file_name = "games/adapters/data/games.csv"
        # reader = GameFileCSVReader(games_file_name)
        # reader.read_csv_file()
        # self.games = reader.dataset_of_games
        # self.genres = reader.dataset_of_genres
        # self.publishers = reader.dataset_of_publishers

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
                    'reviews': game.reviews,
                    'reviews_count': len(game.reviews),
                    'id': game.game_id,
                    'about': game.description
                }
                listofgames.append(Gamepart)
            except:
                pass

        listofgames.sort(key=lambda x: x['name'])
        return listofgames

    def add_game(self, new_game: Game):
        if new_game not in self.games:
            self.games.append(new_game)

    def add_genre_set(self, genre_set):
        if all(isinstance(genre, Genre) for genre in genre_set):
            og_genre_set = set(self.genres)
            og_genre_set.update(og_genre_set - set(genre_set))
            self.genres = list(og_genre_set)

    def add_publisher_set(self, publisher_set):
        if all(isinstance(publisher, Publisher) for publisher in publisher_set):
            og_publisher_set = set(self.publishers)
            og_publisher_set.update(og_publisher_set - set(publisher_set))
            self.publishers = list(og_publisher_set)

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
                        'reviews': game.reviews,
                        'reviews_count': len(game.reviews),
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
                    'reviews': game.reviews,
                    'reviews_count': len(game.reviews),
                    'id': game.game_id,
                    'about': game.description,
                }
                break
        return the_game

    def get_name_search_list(self, listofgames, target):
        search_list = []
        if target != '':
            for game in listofgames:
                if target.lower() in game['name'].lower():
                    search_list.append(game)
        search_list.sort(key=lambda x: x['name'])
        return search_list

    def get_publisher_search_list(self,listofgames,target):
        search_list = []
        if target != '':
            for game in listofgames:
                if target.lower() in game['publishers'].lower():
                    search_list.append(game)
        search_list.sort(key=lambda x: x['publishers'])
        return search_list

    def add_user(self, user: User):
        self.users.append(user)

    def get_user(self, user_name):
        return next((user for user in self.users if user.username == user_name), None)

    def add_game_to_wishlist(self, username: str, game: Game):
        user_wishlist = self._wishlists.get(username)
        if not user_wishlist:
            raise ValueError(f"Wishlist for user {username} not found!")
        user_wishlist.add_game(game)

    def remove_game_from_wishlist(self, username: str, game: Game):
        user_wishlist = self._wishlists.get(username)
        if not user_wishlist:
            raise ValueError(f"Wishlist for user {username} not found!")
        user_wishlist.remove_game(game)

    def get_wishlist(self, username: str) -> Wishlist:
        return self._wishlists.get(username)

    def game_in_wishlist(self, username: str, game: Game) -> bool:
        user_wishlist = self._wishlists.get(username)
        if not user_wishlist:
            raise ValueError(f"Wishlist for user {username} not found!")
        return game in user_wishlist.list_of_games()

    def add_review(self, review: Review):
        if review not in self.reviews:
            self.reviews.append(review)

    def get_all_reviews(self) -> list[Review]:
        return self.reviews

    def get_reviews_by_game(self, game_id: int) -> list[Review]:
        game_reviews = [review for review in self.reviews if review.game_id == game_id]
        return game_reviews

    def get_reviews_by_user(self, user_id: int) -> list[Review]:
        user_reviews = [review for review in self.reviews if review.user_id == user_id]
        return user_reviews

    def delete_review(self, review_id: int):
        self.reviews = [review for review in self.reviews if review.review_id != review_id]

def populate(repo: MemoryRepository):
    dir_name = os.path.dirname(os.path.abspath(__file__))
    games_file_name = os.path.join(dir_name, "data/games.csv")
    reader = GameFileCSVReader(games_file_name)

    reader.read_csv_file()

    games = reader.dataset_of_games
    genres = reader.dataset_of_genres
    publishers = reader.dataset_of_publishers

    for game in games:
        repo.add_game(game)
    repo.add_genre_set(genres)
    repo.add_publisher_set(publishers)
