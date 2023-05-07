from dataclasses import dataclass, field
import uuid

@dataclass(frozen=True)
class UserID:
    value: str = field(default_factory=lambda: str(uuid.uuid4()))