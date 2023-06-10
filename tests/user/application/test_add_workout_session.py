from datetime import date, timedelta
import unittest

from src.user.infrastructure.user_repository import UserRepository
from src.user.application.add_workout_session import get_add_workout_session
from src.user.application.create_user import get_create_user
from src.user.application.find_user import get_find_user


class TestAddWorkoutSession(unittest.TestCase):
    def setUp(self):
        self.repository = UserRepository()
        self.create_user = get_create_user(self.repository)
        self.find_user = get_find_user(self.repository)
        self.add_workout_session = get_add_workout_session(self.repository)

        return super().setUp()

    def test_add_workout_session(self):
        created_user = self.create_user('Adrián', 'adrian@email.com')
        user_id = created_user.get_id()

        self.add_workout_session(user_id, date.today())
        found_user = self.find_user(user_id)
        workout_sessions = found_user.get_workout_sessions()

        self.assertEqual(len(workout_sessions), 1)
