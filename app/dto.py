from dataclasses import dataclass


@dataclass(frozen=True)
class Tutorial:
    tutorial_id: int
    name: str
