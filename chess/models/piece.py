from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from ..constants.enums import PieceType, Player
from .position import Position

if TYPE_CHECKING:
    from .board import Board

class Piece(ABC):
    def __init__(self, piece_type: PieceType, player: Player, position: Position):
        self.piece_type = piece_type
        self.player = player
        self.position = position

    def can_move_to(self, board: 'Board', target: Position) -> bool:
        if not target.is_valid():
            return False

        target_piece = board.get_piece_at(target)
        if target_piece and target_piece.player == self.player:
            return False

        return True