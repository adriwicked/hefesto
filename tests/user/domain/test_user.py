from datetime import date
import unittest

from src.user.domain.user import User
from src.user.domain.user_id import UserID


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(name='Adrián', email='adrian@example.com')

    def test_init(self):
        self.assertIsInstance(self.user._id, UserID)
        self.assertEqual(self.user._name, 'Adrián')
        self.assertEqual(self.user._email, 'adrian@example.com')

    def test_init_user_providing_id(self):
        user_id = UserID()
        user = User(id=user_id, name='Adrián', email='adrian@example.com')
        self.assertEqual(user.get_id(), user_id)

    def test_compare_same_users(self):
        user_id = UserID()
        user1 = User(id=user_id, name='Adrián', email='adrian@example.com')
        user2 = User(id=user_id, name='Cristian', email='cristian@example.com')
        self.assertEqual(user1, user2)

    def test_compare_different_users(self):
        user1 = User(name='Adrián', email='adrian@example.com')
        user2 = User(name='Cristian', email='cristian@example.com')
        self.assertNotEqual(user1, user2)

    def test_get_id(self):
        self.assertIsNotNone(self.user.get_id())

    def test_add_workout_session(self):
        workout_session = date.today()
        self.user.add_workout_session(workout_session)
        workout_sessions = self.user.get_workout_sessions()
        self.assertEqual(len(workout_sessions), 1)
        self.assertEqual(workout_sessions[0], workout_session)

    def test_get_workout_sessions(self):
        self.user.add_workout_session(date.today())
        workout_sessions = self.user.get_workout_sessions()
        self.assertEqual(len(workout_sessions), 1)
        self.assertIsInstance(workout_sessions[0], date)

    def test_add_duplicated_workout_session(self):
        workout_session = date.today()
        self.user.add_workout_session(workout_session)

        with self.assertRaises(ValueError):
            self.user.add_workout_session(workout_session)
