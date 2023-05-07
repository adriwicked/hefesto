class User:
    def __init__(self, name: str, email: str):
        self._name = name
        self._email = email
        self._workout_sessions = []

    def get_workout_sessions(self):
        return self._workout_sessions

    def add_workout_session(self, workout_session):
        if workout_session in self._workout_sessions:
            raise ValueError('The workout session already exists')

        self._workout_sessions.append(workout_session)