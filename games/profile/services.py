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
