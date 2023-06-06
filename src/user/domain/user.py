from datetime import date
from typing import List

from src.user.domain.user_id import UserID


class User:
    def __init__(self, name: str, email: str, id: UserID = None):
        self._id = id if id != None else UserID()
        self._name = name
        self._email = email
        self._workout_sessions = []

    def __eq__(self, other):
        return self._id == other.get_id()

    def __ne__(self, other):
        return self._id != other.get_id()

    def get_id(self) -> UserID:
        return self._id

    def get_workout_sessions(self) -> List[date]:
        return self._workout_sessions

    def add_workout_session(self, workout_session: date):
        assert workout_session not in self._workout_sessions

        self._workout_sessions.append(workout_session)
