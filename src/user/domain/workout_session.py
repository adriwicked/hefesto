from dataclasses import dataclass, field
from datetime import date

@dataclass(frozen=True)
class WorkoutSession:
    value: date = field(default_factory=lambda: date.today())

    def __eq__(self, other):
        return self.value == other.value