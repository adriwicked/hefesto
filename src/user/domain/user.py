class User:
    def __init__(
        self,
        name: str,
        email: str
    ):
        self.name = name
        self.email = email
        self.workout_sessions = []

    def add_workout_session(self, workout_session):
        if workout_session in self.workout_sessions:
            raise ValueError('The workout session already exists')
        
        self.workout_sessions.append(workout_session)