from games.adapters.Abstract_class import AbstractRepository


def get_games(repo: AbstractRepository):
    my_list = repo.get_all_games()
    smaller_list = my_list[:3]
    return smaller_list


def get_unique_genres(repo: AbstractRepository):
    return repo.get_unique_genres()


# In your services.py or wherever you store your services

# In your services.py or equivalent file

def get_user_details_by_username(username, repo):
    """
    Fetch user details by a given username from the memory repository.
    """
    user = repo.get_user(username)
    if user:
        # Convert the User object to dictionary or another structure if necessary.
        return user  # Adjust this based on how you're using the user object in your templates.
    raise ValueError("User not found")

def get_games(repo):
    """
    Fetch all games from the memory repository.
    """
    return repo.get_all_games()

def get_wishlist_by_username(username, repo):
    """
    Fetch games in the wishlist of a given username from the memory repository.
    """
    wishlist = repo.get_wishlist(username)
    if wishlist:
        # Convert the wishlist games to the desired format
        # Here I'm assuming that your wishlist object has a list_of_games method
        # that returns the games in the wishlist.
        games = wishlist.list_of_games()
        # Convert the games to the desired format if necessary
        return games
    return []


def remove_game_from_wishlist(repo: AbstractRepository, game_id: int):
    return repo.remove_game_from_wishlist(game_id)


def get_unique_genres(repo: AbstractRepository):
    return repo.get_unique_genres()

def get_game_by_id(repo: AbstractRepository, game_id: int):
    return repo.get_game_by_id(game_id)

def get_wishlist(username, repo: AbstractRepository):
    """
    Fetch games in the wishlist of a given username from the memory repository.
    """

    wishlist = repo.get_wishlist(username)
    if wishlist:
        # Convert the wishlist games to the desired format
        # Here I'm assuming that your wishlist object has a list_of_games method
        # that returns the games in the wishlist.
        games = wishlist.list_of_games()
        # Convert the games to the desired format if necessary
        return games
    return []

def get_user_details_by_username(username, repo):
    """
    Fetch user details by a given username from the memory repository.
    """
    user = repo.get_user(username)
    if user:
        # Convert the User object to dictionary or another structure if necessary.
        return user  # Adjust this based on how you're using the user object in your templates.
    raise ValueError("User not found")


def get_game_description(repo: AbstractRepository, game_id):
    return repo.get_game_description(game_id)

def get_wishlist_description(repo: AbstractRepository, wishlist):
    wishlist_description = []
    for game in wishlist:
        game_id = game.game_id
        current = get_game_description(repo, game_id)
        wishlist_description.append(current)
    return wishlist_description
