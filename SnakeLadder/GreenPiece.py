from PieceType import PieceType
from PlayingPiece import PlayingPiece

class GreenPiece(PlayingPiece):

    def __init__(self, playingPiece = PieceType.GREEN) -> None:
        super().__init__(playingPiece)