from dataclasses import dataclass


@dataclass(frozen=True)
class Tutorial:
    name: str
    tutorial_id: int = 0
