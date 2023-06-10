from datetime import date

from src.user.domain.user_id import UserID
from src.user.infrastructure.user_repository import UserRepository


def get_add_workout_session(repository: UserRepository):
    def add_workout_session(user_id: UserID, date: date):
        found_user = repository.find(user_id)

        if not found_user:
            return

        found_user.add_workout_session(date)
        repository.save(found_user)

    return add_workout_session