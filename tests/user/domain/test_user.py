from datetime import date
import unittest

from src.user.domain.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(name='Adrián', email='adrian@example.com')

    def test_init(self):
        self.assertEqual(self.user._name, 'Adrián')
        self.assertEqual(self.user._email, 'adrian@example.com')

    def test_get_workout_sessions(self):
        self.assertEqual(self.user.get_workout_sessions(), [])

    def test_add_workout_session(self):
        workout_session = date.today()
        self.user.add_workout_session(workout_session)
        workout_sessions = self.user.get_workout_sessions()
        self.assertEqual(len(workout_sessions), 1)
        self.assertEqual(workout_sessions[0], workout_session)

    def test_add_duplicated_workout_session(self):
        workout_session = date.today()
        self.user.add_workout_session(workout_session)

        with self.assertRaises(ValueError):
            self.user.add_workout_session(workout_session)
