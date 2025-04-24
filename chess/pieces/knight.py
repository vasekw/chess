from ..models.piece import Piece
from ..models.position import Position
from ..constants.enums import PieceType, Player

class Knight(Piece):
    def __init__(self, player: Player, position: Position):
        super().__init__(piece_type=PieceType.KNIGHT, player=player, position=position)

    def can_move_to(self, board: 'Board', target: Position) -> bool:
        if not super().can_move_to(board, target):
            return False

        dx = abs(target.x - self.position.x)
        dy = abs(target.y - self.position.y)
        return (dy, dx) in [(1,2), (2,1)]