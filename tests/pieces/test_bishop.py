import pytest
from chess.models.board import Board
from chess.models.position import Position
from chess.constants.enums import Player
from chess.pieces.bishop import Bishop


@pytest.fixture
def board_with_bishop():
    board = Board()
    start_pos = Position(3, 3)
    bishop = Bishop(Player.WHITE, start_pos)
    board.add_piece(bishop)
    return board, bishop


@pytest.mark.parametrize("target_pos", [
    Position(1, 1),  # diagonal down-left
    Position(5, 5),  # diagonal up-right
    Position(1, 5),  # diagonal up-left
    Position(5, 1)  # diagonal down-right
])
def test_valid_moves(board_with_bishop, target_pos):
    board, bishop = board_with_bishop
    assert bishop.can_move_to(board, target_pos)


@pytest.mark.parametrize("target_pos", [
    Position(3, 5),  # vertical
    Position(5, 3),  # horizontal
    Position(4, 2),  # non-diagonal
    Position(8, 8)  # off board
])
def test_invalid_moves(board_with_bishop, target_pos):
    board, bishop = board_with_bishop
    assert not bishop.can_move_to(board, target_pos)


def test_blocked_moves(board_with_bishop):
    board, bishop = board_with_bishop

    # Place blocking piece
    blocking_pos = Position(4, 4)
    blocking_piece = Bishop(Player.WHITE, blocking_pos)
    board.add_piece(blocking_piece)

    # Try to move past blocking piece
    target_pos = Position(5, 5)
    assert not bishop.can_move_to(board, target_pos)


def test_capture_moves(board_with_bishop):
    board, bishop = board_with_bishop

    # Test capturing enemy piece
    capture_pos = Position(5, 5)
    enemy_piece = Bishop(Player.BLACK, capture_pos)
    board.add_piece(enemy_piece)
    assert bishop.can_move_to(board, capture_pos)

    # Test cannot capture friendly piece
    friendly_pos = Position(1, 1)
    friendly_piece = Bishop(Player.WHITE, friendly_pos)
    board.add_piece(friendly_piece)
    assert not bishop.can_move_to(board, friendly_pos)