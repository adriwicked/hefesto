from datetime import date
import unittest

from src.user.domain.user import User
from src.user.infrastructure.user_repository import UserRepository


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.repo = UserRepository()

    def test_save_user_returns_saved_user(self):
        user = User(name='Adrián', email='adrian@example.com')
        saved_user = self.repo.save(user)
        self.assertEqual(saved_user, user)

    def test_update_user(self):
        user = User(name='Adrián', email='adrian@example.com')
        self.repo.save(user)

        found_user = self.repo.find(user.get_id())
        found_user.add_workout_session(date.today())
        self.repo.save(found_user)

        updated_user = self.repo.find(user.get_id())
        workout_sessions = updated_user.get_workout_sessions()
        users = self.repo.findAll()

        self.assertEqual(len(workout_sessions), 1)
        self.assertEqual(len(users), 1)

    def test_get_user_by_id(self):
        user = User(name='Adrián', email='adrian@example.com')
        self.repo.save(user)
        obtained_user = self.repo.find(user.get_id())
        self.assertEqual(user, obtained_user)

    def test_get_user_by_id_raise_error_if_id_not_provided(self):
        with self.assertRaises(AssertionError):
            self.repo.find(None)
