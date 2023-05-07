from datetime import date
import unittest

from src.user.domain.user import User


class TestUser(unittest.TestCase):
    def test_init(self):
        user = User(name='Adrián', email='adrian@example.com')
        self.assertEqual(user.name, 'Adrián')
        self.assertEqual(user.email, 'adrian@example.com')

    def test_add_workout_session(self):
        user = User(name='Adrián', email='adrian@example.com')
        workout_session = date.today()
        user.add_workout_session(workout_session)
        self.assertEqual(len(user.workout_sessions), 1)
        self.assertEqual(user.workout_sessions[0], workout_session)

    def test_add_duplicated_workout_session(self):
        user = User(name='Adrián', email='adrian@example.com')
        workout_session = date.today()
        user.add_workout_session(workout_session)

        with self.assertRaises(ValueError):
            user.add_workout_session(workout_session)
