from src.user.domain.user import User
from src.user.infrastructure.user_repository import UserRepository


def get_create_user(repo: UserRepository):
    def create_user(name, email):
        assert name and email

        user = User(name, email)
        return repo.save(user)

    return create_user