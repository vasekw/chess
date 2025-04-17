from typing import Optional, Dict
from .position import Position
from .piece import Piece
from ..constants.enums import Player

class Board:
    def __init__(self):
        self.pieces: Dict[Position, Piece] = {}

    def add_piece(self, piece: Piece) -> None:
        if not piece.position.is_valid():
            raise ValueError("Invalid position")
        self.pieces[piece.position] = piece

    def get_piece_at(self, position: Position) -> Optional[Piece]:
        return self.pieces.get(position)

    def move_piece(self, from_pos: Position, to_pos: Position, player: Player) -> bool:
        if not from_pos.is_valid() or not to_pos.is_valid():
            return False

        piece = self.get_piece_at(from_pos)
        if not piece or piece.player != player:
            return False

        if not piece.can_move_to(self, to_pos):
            return False

        del self.pieces[from_pos]
        piece.position = to_pos
        self.pieces[to_pos] = piece

        return True

    def clear(self):
        self.pieces.clear()