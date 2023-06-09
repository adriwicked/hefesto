import unittest
from datetime import date, timedelta

from src.user.domain.workout_session import WorkoutSession


class TestWorkoutSession(unittest.TestCase):
    def test_workout_session_value(self):
        workout_session = WorkoutSession()
        self.assertIsNotNone(workout_session.value)
        self.assertIsInstance(workout_session.value, date)

    def test_create_workout_session_with_specific_date(self):
        today = date.today()
        workout_session = WorkoutSession(today)
        self.assertEqual(workout_session.value, today)

    def test_compare_same_workout_sessions(self):
        today = date.today()
        ws1 = WorkoutSession(today)
        ws2 = WorkoutSession(today)
        self.assertEqual(ws1, ws2)

    def test_compare_different_workout_sessions(self):
        today = date.today()
        yesterday = today - timedelta(days=1)
        ws1 = WorkoutSession(today)
        ws2 = WorkoutSession(yesterday)
        self.assertNotEqual(ws1, ws2)