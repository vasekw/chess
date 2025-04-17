import pytest
from chess.models.position import Position

def test_position_creation():
    pos = Position(3, 4)
    assert pos.x == 3
    assert pos.y == 4

@pytest.mark.parametrize("x,y,expected", [
    (0, 0, True),
    (7, 7, True),
    (3, 4, True),
    (-1, 0, False),
    (0, -1, False),
    (8, 0, False),
    (0, 8, False),
])
def test_position_validity(x, y, expected):
    pos = Position(x, y)
    assert pos.is_valid() == expected

def test_position_equality():
    pos1 = Position(1, 2)
    pos2 = Position(1, 2)
    pos3 = Position(2, 1)

    assert pos1 == pos2
    assert pos1 != pos3
    assert hash(pos1) == hash(pos2)
    assert len({pos1, pos2}) == 1