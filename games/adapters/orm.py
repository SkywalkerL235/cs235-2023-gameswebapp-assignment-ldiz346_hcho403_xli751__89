from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Text, Float, ForeignKey, DateTime, func
)
from sqlalchemy.orm import mapper, relationship

from games.domainmodel.model import Game, Publisher, Genre, User, Review, Wishlist

# global variable giving access to the MetaData (schema) information of the database
metadata = MetaData()

publishers_table = Table(
    'publishers', metadata,
    # We only want to maintain those attributes that are in our domain model
    # For publisher, we only have name
    Column('name', String(255), primary_key=True, nullable=False, unique=True)
)

games_table = Table(
    'games', metadata,
    Column('game_id', Integer, primary_key=True, unique=True),
    Column('game_title', Text, nullable=False),
    Column('game_price', Float, nullable=False),
    Column('release_date', String(50), nullable=False),
    Column('game_description', String(255), nullable=True),
    Column('game_image_url', String(255), nullable=True),
    Column('game_website_url', String(255), nullable=True),
    Column('publisher_name', ForeignKey('publishers.name'))
)

genres_table = Table(
    'genres', metadata,
    # For genre, we only have name
    Column('genre_name', String(64), primary_key=True, nullable=False),
)

user_table = Table(
    'users', metadata,
    Column('user_id', Integer, primary_key=True, autoincrement=True),
    Column('user_username', String(20), unique=True, nullable=False),
    Column('user_password', String(20), nullable=False),
)

review_table = Table(
    'reviews', metadata,
    Column('review_id', Integer, primary_key=True, autoincrement=True),
    Column('timestamp', DateTime, nullable=False, server_default=func.now()),
    Column('user_id', Integer, ForeignKey('users.user_id'), nullable=False),
    Column('game_id', Integer, ForeignKey('games.game_id'), nullable=False),
    Column('rating', Integer, nullable=False),
    Column('comment', String(255), nullable=True)
)

game_genres_table = Table(
    'game_genres', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('game_id', ForeignKey('games.game_id')),
    Column('genre_name', ForeignKey('genres.genre_name'))
)

wishlist_table = Table(
    'wishlists', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', Integer, ForeignKey('users.user_id'),unique=True, nullable=False,),
)
game_wishlist_table = Table(
    'wishlist_game', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('game_id', Integer, ForeignKey('games.game_id')),
    Column('wishlist_id', Integer, ForeignKey('wishlists.id')),  # This should reference the primary key of wishlists table
)


def map_model_to_tables():
    mapper(Publisher, publishers_table, properties={
        '_Publisher__publisher_name': publishers_table.c.name,
    })

    mapper(Game, games_table, properties={
        '_Game__game_id': games_table.c.game_id,
        '_Game__game_title': games_table.c.game_title,
        '_Game__price': games_table.c.game_price,
        '_Game__release_date': games_table.c.release_date,
        '_Game__description': games_table.c.game_description,
        '_Game__image_url': games_table.c.game_image_url,
        '_Game__website_url': games_table.c.game_website_url,
        '_Game__publisher': relationship(Publisher),
        '_Game__genres': relationship(Genre, secondary=game_genres_table),
        '_Game__reviews': relationship(Review, back_populates='_Review__game')
    })

    mapper(Genre, genres_table, properties={
        '_Genre__genre_name': genres_table.c.genre_name,
    })

    mapper(Review, review_table, properties={
        '_Review__timestamp': review_table.c.timestamp,
        '_Review__review_id': review_table.c.review_id,
        '_Review__user': relationship(User, back_populates='_User__reviews'),
        '_Review__game': relationship(Game, back_populates='_Game__reviews'),
        '_Review__rating': review_table.c.rating,
        '_Review__comment': review_table.c.comment,
    })

    mapper(User, user_table, properties={
        '_User__user_id': user_table.c.user_id,
        '_User__username': user_table.c.user_username,
        '_User__password': user_table.c.user_password,
        '_User__reviews': relationship(Review, back_populates='_Review__user'),
        '_User__wishlist': relationship(Wishlist, uselist=False, back_populates="_Wishlist__user"),
        # one-to-one relationship with Wishlist
    })

    mapper(Wishlist, wishlist_table, properties={
        '_Wishlist__id': wishlist_table.c.id,
        '_Wishlist__user': relationship(User, back_populates="_User__wishlist"),  # corresponding back_populates
        '_Wishlist__list_of_games': relationship(
            Game,
            secondary=game_wishlist_table,
            primaryjoin=(wishlist_table.c.id == game_wishlist_table.c.wishlist_id),
            secondaryjoin=(games_table.c.game_id == game_wishlist_table.c.game_id),
        )
    })
