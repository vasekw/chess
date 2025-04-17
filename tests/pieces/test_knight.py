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
    # Test valid position
    board.add_piece(knight)
    assert knight.can_move_to(board, Position(4, 4))  # Any valid board position should return True


def test_knight_invalid_position(board, knight):
    board.add_piece(knight)
    assert not knight.can_move_to(board, Position(8, 8))  # Off board position


def test_knight_capture_validation(board, knight):
    board.add_piece(knight)

    # Test capturing enemy piece (should be allowed)
    enemy_pos = Position(4, 4)
    enemy_piece = Knight(Player.BLACK, enemy_pos)
    board.add_piece(enemy_piece)
    assert knight.can_move_to(board, enemy_pos)

    # Test capturing friendly piece (should not be allowed)
    friendly_pos = Position(5, 5)
    friendly_piece = Knight(Player.WHITE, friendly_pos)
    board.add_piece(friendly_piece)
    assert not knight.can_move_to(board, friendly_pos)