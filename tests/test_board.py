import pytest
from chess.models.board import Board
from chess.models.position import Position
from chess.constants.enums import Player
from chess.pieces.bishop import Bishop
from chess.pieces.knight import Knight


@pytest.fixture
def empty_board():
    return Board()


@pytest.fixture
def valid_position():
    return Position(3, 3)


@pytest.fixture
def invalid_position():
    return Position(8, 8)


def test_add_piece(empty_board, valid_position):
    piece = Bishop(Player.WHITE, valid_position)
    empty_board.add_piece(piece)
    assert empty_board.get_piece_at(valid_position) == piece


def test_add_piece_invalid_position(empty_board, invalid_position):
    piece = Bishop(Player.WHITE, invalid_position)
    with pytest.raises(ValueError):
        empty_board.add_piece(piece)


def test_get_piece_at(empty_board, valid_position):
    piece = Bishop(Player.WHITE, valid_position)
    empty_board.add_piece(piece)

    assert empty_board.get_piece_at(valid_position) == piece
    assert empty_board.get_piece_at(Position(0, 0)) is None


def test_move_piece(empty_board):
    start_pos = Position(0, 0)
    end_pos = Position(2, 2)
    piece = Bishop(Player.WHITE, start_pos)
    empty_board.add_piece(piece)

    assert empty_board.move_piece(start_pos, end_pos, Player.WHITE)
    assert empty_board.get_piece_at(start_pos) is None
    assert empty_board.get_piece_at(end_pos) == piece


def test_move_piece_invalid_cases(empty_board):
    start_pos = Position(0, 0)
    end_pos = Position(2, 2)
    piece = Bishop(Player.WHITE, start_pos)
    empty_board.add_piece(piece)

    # Wrong player
    assert not empty_board.move_piece(start_pos, end_pos, Player.BLACK)

    # Invalid positions
    assert not empty_board.move_piece(Position(8, 8), end_pos, Player.WHITE)
    assert not empty_board.move_piece(start_pos, Position(8, 8), Player.WHITE)


def test_clear(empty_board):
    piece1 = Bishop(Player.WHITE, Position(0, 0))
    piece2 = Knight(Player.BLACK, Position(1, 1))

    empty_board.add_piece(piece1)
    empty_board.add_piece(piece2)

    empty_board.clear()
    assert len(empty_board.pieces) == 0