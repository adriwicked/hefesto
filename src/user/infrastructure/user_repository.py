from src.user.domain.user import User
from src.user.domain.user_id import UserID


class UserRepository:
    def __init__(self) -> None:
        self.users = []

    def save(self, user: User) -> User:
        found_user = self.find(id=user.get_id())

        if not found_user:
            self.users.append(user)

        return user

    def find(self, id: UserID) -> User:
        assert id

        for user in self.users:
            if user.get_id() == id:
                return user
        return None

    def findAll(self):
        return self.users
