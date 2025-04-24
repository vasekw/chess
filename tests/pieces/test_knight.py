import pytest
from chess.models.board import Board
from chess.models.position import Position
from chess.constants.enums import Player
from chess.pieces.knight import Knight
from chess.constants.enums import PieceType


@pytest.fixture
def board():
    return Board()


@pytest.fixture
def knight():
    return Knight(Player.WHITE, Position(3, 3))


def test_knight_creation(knight):
    assert knight.player == Player.WHITE
    assert knight.position == Position(3, 3)
    assert knight.piece_type == PieceType.KNIGHT


def test_knight_basic_move_validation(board, knight):
    board.add_piece(knight)
    assert knight.can_move_to(board, Position(5, 4))  # Example valid L-shaped move


def test_knight_invalid_position(board, knight):
    board.add_piece(knight)
    assert not knight.can_move_to(board, Position(8, 8))  # Off the board


def test_knight_capture_validation(board, knight):
    board.add_piece(knight)

    enemy_pos = Position(5, 4)
    enemy_piece = Knight(Player.BLACK, enemy_pos)
    board.add_piece(enemy_piece)
    assert knight.can_move_to(board, enemy_pos)

    friendly_pos = Position(5, 2)
    friendly_piece = Knight(Player.WHITE, friendly_pos)
    board.add_piece(friendly_piece)
    assert not knight.can_move_to(board, friendly_pos)


@pytest.mark.parametrize("target_pos", [
    Position(5, 4),
    Position(5, 2),
    Position(4, 5),
    Position(2, 5),
    Position(1, 4),
    Position(1, 2),
    Position(2, 1),
    Position(4, 1),
])
def test_knight_all_valid_moves(board, knight, target_pos):
    board.add_piece(knight)
    assert knight.can_move_to(board, target_pos)


@pytest.mark.parametrize("target_pos", [
    Position(3, 4),  # Horizontal
    Position(3, 2),
    Position(4, 3),  # Vertical
    Position(2, 3),
    Position(4, 4),  # Diagonal
    Position(2, 2),
    Position(0, 0),  # Too far
    Position(10, 10),
])
def test_knight_invalid_moves(board, knight, target_pos):
    board.add_piece(knight)
    assert not knight.can_move_to(board, target_pos)
