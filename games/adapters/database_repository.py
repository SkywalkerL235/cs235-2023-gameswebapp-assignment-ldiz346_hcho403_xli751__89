from abc import ABC
from typing import List

from sqlalchemy import func, or_
from sqlalchemy.orm import scoped_session, session
from sqlalchemy.orm.exc import NoResultFound

from games.adapters.Abstract_class import AbstractRepository
from games.adapters.utils import search_string
from games.domainmodel.model import Game, Publisher, Genre, User, Review, Wishlist


class SessionContextManager:
    def __init__(self, session_factory):
        self.__session_factory = session_factory
        self.__session = scoped_session(self.__session_factory)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @property
    def session(self):
        return self.__session

    def commit(self):
        self.__session.commit()

    def rollback(self):
        self.__session.rollback()

    def reset_session(self):
        # this method can be used e.g. to allow Flask to start a new session for each http request,
        # via the 'before_request' callback
        self.close_current_session()
        self.__session = scoped_session(self.__session_factory)

    def close_current_session(self):
        if self.__session is not None:
            self.__session.close()


class SqlAlchemyRepository(AbstractRepository, ABC):

    def __init__(self, session_factory):
        self._session_cm = SessionContextManager(session_factory)

    def close_session(self):
        self._session_cm.close_current_session()

    def reset_session(self):
        self._session_cm.reset_session()

    # region User_data

    def add_user(self, user: User):
        with self._session_cm as scm:
            scm.session.merge(user)
            scm.commit()

    def get_user(self, user_name: str) -> User:
        user = None
        try:
            user = self._session_cm.session.query(User).filter(User._User__username == user_name).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass

        return user

    # endregion

    # region Game_data

    def get_game_by_id(self, game_id: int) -> Game:
        game = self._session_cm.session.query(Game).filter(Game._Game__game_id == game_id).one()
        return game

    def get_games(self) -> List[Game]:
        games = self._session_cm.session.query(Game).order_by(Game._Game__game_id).all()
        return games

    def search_games_by_title(self, title_string: str) -> List[Game]:
        games = self._session_cm.session.query(Game).filter(Game._Game__game_title).all()
        return games

    def get_game_description(self, game_id: int) -> dict:
        the_game = None
        try:
            game = self._session_cm.session.query(
                Game).filter(Game._Game__game_id == game_id).one()
            print(game)

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
                'id': game.game_id,
                'about': game.description,
            }
        except NoResultFound:
            print(f'Game {game_id} was not found')

        return the_game

    def add_game(self, game: Game):
        with self._session_cm as scm:
            scm.session.merge(game)
            scm.commit()

    def add_multiple_games(self, games: List[Game]):
        with self._session_cm as scm:
            for game in games:
                scm.session.merge(game)
            scm.commit()

    def get_number_of_games(self):
        total_games = self._session_cm.session.query(Game).count()
        return total_games

    def get_all_games(self):
        listofgames = []

        games = self._session_cm.session.query(Game).all()

        for game in games:
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
                    'id': game.game_id,
                    'about': game.description
                }
                listofgames.append(Gamepart)
            except:
                pass

        listofgames.sort(key=lambda x: x['name'])
        return listofgames

    def filter_by_genre(self, selected_genre) -> list[Game]:
        listofgames = []
        games = self._session_cm.session.query(Game).filter(Game._Game__genres.any(func.lower(Genre._Genre__genre_name) == func.lower(selected_genre)))
        for game in games:
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
                    'id': game.game_id,
                    'about': game.description
                }
                listofgames.append(Gamepart)
            except:
                pass

        listofgames.sort(key=lambda x: x['name'])
        return listofgames

    def get_name_search_list(self, listofgames, target):
        search_list = []

        # Use ilike for case-insensitive search
        ilike_target = '%' + target + '%'

        for game in listofgames:
            game_title = game['name']

            # case-insensitive search
            query = func.lower(game_title).like(func.lower(ilike_target))
            if self._session_cm.session.query(Game).filter(or_(query)).count() > 0:
                search_list.append(game)

        search_list.sort(key=lambda x: x['name'])
        return search_list

    # endregion

    # region Publisher data

    def get_publishers(self) -> List[Publisher]:
        pass

    def add_publisher(self, publisher: Publisher):
        with self._session_cm as scm:
            scm.session.merge(publisher)
            scm.commit()

    def add_multiple_publishers(self, publishers: List[Publisher]):
        with self._session_cm as scm:
            for publisher in publishers:
                scm.session.merge(publisher)
            scm.commit()

    def add_publisher_set(self, publisher_set):
        if all(isinstance(publisher, Publisher) for publisher in publisher_set):
            with self._session_cm as scm:
                for publisher in publisher_set:
                    scm.session.merge(publisher)
                scm.commit()

    def get_number_of_publishers(self) -> int:
        pass

    def get_publisher_search_list(self, listofgames, target):
        search_list = []

        # Use ilike for case-insensitive search
        ilike_target = '%' + target + '%'

        for game in listofgames:
            game_publisher = game['publishers']

            # case-insensitive search
            query = func.lower(game_publisher).like(func.lower(ilike_target))
            if self._session_cm.session.query(Game).filter(or_(query)).count() > 0:
                search_list.append(game)

        search_list.sort(key=lambda x: x['name'])
        return search_list

    # endregion

    # region Genre_data

    def get_unique_genres(self) -> List[Genre]:
        genre_names = []
        genres = self._session_cm.session.query(Genre).order_by(Genre._Genre__genre_name).all()
        for genre in genres:
            genre_names.append(genre.genre_name)
        return genre_names

    def add_genre(self, genre: Genre):
        with self._session_cm as scm:
            scm.session.merge(genre)
            scm.commit()

    def add_multiple_genres(self, genres: List[Genre]):
        with self._session_cm as scm:
            for genre in genres:
                scm.session.merge(genre)
            scm.commit()

    def add_genre_set(self, genre_set):
        if all(isinstance(genre, Genre) for genre in genre_set):
            with self._session_cm as scm:
                for genre in genre_set:
                    scm.session.merge(genre)
                scm.commit()

    # endregion

    # region Review.data

    def add_review(self, review: Review):
        with self._session_cm as scm:
            scm.session.add(review)
            scm.commit()

    def get_all_reviews(self) -> list[Review]:
        reviews = self._session_cm.session.query(Review).all()
        return reviews

    def get_reviews_by_game(self, game: Game) -> list[Review]:
        game_id = game.game_id
        reviews = self._session_cm.session.query(Review).filter(Game._Game__game_id == game_id).all()
        return reviews

    def get_reviews_by_user(self, user_id: int) -> list[Review]:
        reviews = self._session_cm.session.query(Review).filter(Review._Review__user_id == user_id).all()
        return reviews

    def form_review(self, review: Review):
        user = str(review.user)
        the_review = {
            'user_name': user[6:-1],
            'rating': review.rating,
            'comment': review.comment,
        }
        return the_review

    # endregion

    # region Wishlist_data

    def add_game_to_wishlist(self, username: str, game: Game):
        user = self.get_user(username)
        wishlist = Wishlist(user)
        wishlist.add_game(game)

        with self._session_cm as scm:
            scm.session.add(wishlist)
            scm.commit()

    def remove_game_from_wishlist(self, username: str, game: Game):
        user = self.get_user(username)
        wishlist = Wishlist(user)
        wishlist.add_game(game)
        session.delete(wishlist)

    def get_wishlist(self, username: str) -> Wishlist:
        user_id = self._session_cm.session.query(User).filter(User._User__user_name == username)
        user = self.get_user(username)
        games = self._session_cm.session.query(Game).filter(Wishlist._Wishlist__user_id == user_id).all
        wishlist = Wishlist(user)
        for game in games:
            wishlist.add_game(game)
        return wishlist

    def game_in_wishlist(self, username: str, game: Game) -> bool:
        user_id = self._session_cm.session.query(User).filter(User._User__user_name == username)
        games = self._session_cm.session.query(Wishlist).filter(Wishlist._Wishlist__user_id == user_id).all

        if game in games:
            return True
        return False

    # endregion
