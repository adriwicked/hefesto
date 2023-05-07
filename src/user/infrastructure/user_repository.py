from src.user.domain.user import User
from src.user.domain.user_id import UserID


class UserRepository:
    def __init__(self) -> None:
        self.users = []

    def save(self, user: User) -> User:
        self.users.append(user)
        return user

    def find(self, id: UserID) -> User:
        for user in self.users:
            if user.get_id() == id:
                return user
        return None