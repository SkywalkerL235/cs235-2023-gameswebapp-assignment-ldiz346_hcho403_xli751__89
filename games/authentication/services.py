from werkzeug.security import generate_password_hash, check_password_hash
from games.adapters.Abstract_class import AbstractRepository
from games.domainmodel.model import User


class NameNotUniqueException(Exception):
    pass


class UnknownUserException(Exception):
    pass


class AuthenticationException(Exception):
    pass


def make_user_dict(user: User):
    user_dict = {
        'user_name': user.username,
        'password': user.password
    }
    return user_dict


def add_user(username: str, password: str, repo: AbstractRepository):
    # Check availability
    user = repo.get_user(username)
    if user is not None:
        raise NameNotUniqueException

    # Password encryption
    password_hash = generate_password_hash(password)

    # Create & store
    user = User(username, password_hash)
    repo.add_user(user)


def get_user(username: str, repo: AbstractRepository):
    user = repo.get_user(username)
    if user is None:
        raise UnknownUserException

    return make_user_dict(user)


def authenticate_user(user_name: str, password: str, repo: AbstractRepository):
    authenticated = False

    user = repo.get_user(user_name)
    if user is not None:
        authenticated = check_password_hash(user.password, password)
    if not authenticated:
        raise AuthenticationException
