from ..models.piece import Piece
from ..models.position import Position
from ..constants.enums import PieceType, Player

class Knight(Piece):
    def __init__(self, player: Player, position: Position):
        super().__init__(piece_type=PieceType.KNIGHT, player=player, position=position)
