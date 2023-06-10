from src.user.infrastructure.user_repository import UserRepository
from src.user.domain.user_id import UserID


def get_find_user(repo: UserRepository):
    def find_user(user_id: UserID):
        assert user_id

        return repo.find(user_id)

    return find_user