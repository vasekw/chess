from typing import List

from ..models.board import Board
from ..models.piece import Piece
from ..models.position import Position
from ..constants.enums import PieceType, Player

class Bishop(Piece):
    def __init__(self, player: Player, position: Position):
        super().__init__(piece_type=PieceType.BISHOP, player=player, position=position)

    def can_move_to(self, board: 'Board', target: Position) -> bool:
        if not super().can_move_to(board, target):
            return False

        dx = abs(target.x - self.position.x)
        dy = abs(target.y - self.position.y)
        if dx != dy:
            return False

        path = self._get_path_positions(target)
        for pos in path[:-1]:
            if board.get_piece_at(pos) is not None:
                return False

        return True

    def _get_path_positions(self, target: Position) -> List[Position]:
        positions = []
        dx = 1 if target.x > self.position.x else -1
        dy = 1 if target.y > self.position.y else -1

        current_x = self.position.x + dx
        current_y = self.position.y + dy

        while current_x != target.x or current_y != target.y:
            positions.append(Position(current_x, current_y))
            current_x += dx
            current_y += dy

        positions.append(target)
        return positions