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
    response = client.get('/game/435790')
    assert response.status_code == 200

def test_service_retrieves_correct_number_of_games(client):
    response = client.get('/games')
    assert response.status_code == 200

def test_paginated_games(client):
    response1 = client.get('/games?page=1')
    response2 = client.get('/games?page=20')
    response3 = client.get('/games?page=39')
    assert response1.status_code == 200
    assert response2.status_code == 200
    assert response3.status_code == 200

def test_filter_games_by_genre(client):
    response = client.get('/filtered_games/Action')
    assert response.status_code == 200

def test_search_games_by_genre(client):
    response = client.get('/g_search')
    assert response.status_code == 200

def test_search_games_by_name(client):
    response = client.post('/n_search', data={'search': '10 Second Ninja X'})
    assert response.status_code == 200

def test_search_games_by_non_existing_name(client):
    response = client.post('/n_search', data={'search': '#%$@*'})
    assert response.status_code == 200

def test_search_games_by_publisher(client):
    response = client.post('/p_search', data={'search': '8floor'})
    assert response.status_code == 200

def test_search_games_by_non_existing_publisher(client):
    response = client.post('/p_search', data={'search': 'Non-existing Publisher'})
    assert response.status_code == 200
