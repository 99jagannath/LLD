
from PieceType import PieceType
from PlayingPiece import PlayingPiece

class RedPiece(PlayingPiece):

    def __init__(self, playingPiece = PieceType.BLUE) -> None:
        super().__init__(playingPiece)