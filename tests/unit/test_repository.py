import pytest
from games.adapters.Repository_class import MemoryRepository
from games.domainmodel.model import Publisher, Genre, Game, Review, User, Wishlist
from games.adapters.datareader.csvdatareader import GameFileCSVReader
@pytest.fixture
def empty_repository():
    return MemoryRepository()


def test_empty_repository_can_add_game(empty_repository):
    game = Game(1, "Game 1")
    empty_repository.add_game(game)
    assert game in empty_repository.games


def test_empty_repository_can_add_and_retrieve_game(empty_repository):
    game = Game(1, "Game 1")
    empty_repository.add_game(game)

    retrieved_game = empty_repository.get_game_by_id(1)
    assert retrieved_game is not None
    assert retrieved_game.game_id == 1


def test_empty_repository_returns_empty_list(empty_repository):
    games = empty_repository.get_all_games()
    assert len(games) == 0


def test_empty_repository_returns_empty_unique_genres_list(empty_repository):
    unique_genres = empty_repository.get_unique_genres()
    assert len(unique_genres) == 0


def test_empty_repository_returns_empty_search_results(empty_repository):
    listofgames = empty_repository.get_all_games()
    search_results = empty_repository.get_name_search_list(listofgames,"Game 1")
    assert len(search_results) == 0


def test_empty_repository_returns_empty_publisher_search_results(empty_repository):
    listofgames = empty_repository.get_all_games()
    search_results = empty_repository.get_publisher_search_list(listofgames,"Publisher 1")
    assert len(search_results) == 0

