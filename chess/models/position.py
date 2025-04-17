from dataclasses import dataclass

@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def is_valid(self) -> bool:
        return 0 <= self.x < 8 and 0 <= self.y < 8

    def __hash__(self):
        return hash((self.x, self.y))