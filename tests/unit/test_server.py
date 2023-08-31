import pytest
from games.adapters.Repository_class import MemoryRepository
from games.__init__ import create_app

@pytest.fixture
def client():
    repository = MemoryRepository()
    app = create_app(repository)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_service_returns_existing_game(client):
    response = client.get('/game/1')
    assert b'Game 1' in response.data

def test_service_retrieves_correct_number_of_games(client):
    response = client.get('/games')
    assert b'Number of Games: 2' in response.data

def test_paginated_games(client):
    response = client.get('/games')
    assert b'Game 1' in response.data
    assert b'Game 2' in response.data

def test_filter_games_by_genre(client):
    response = client.get('/filtered_games/Action')
    assert b'Filtered Games by Genre: Action' in response.data

def test_search_games_by_genre(client):
    response = client.post('/N_search', data={'search': 'Game 1'})
    assert b'Results for Game 1' in response.data

def test_search_games_by_publisher(client):
    response = client.post('/P_search', data={'search': 'Publisher 1'})
    assert b'Results for Publisher 1' in response.data

def test_search_games_by_non_existing_publisher(client):
    response = client.post('/P_search', data={'search': 'Non-existing Publisher'})
    assert b'No results found' in response.data
