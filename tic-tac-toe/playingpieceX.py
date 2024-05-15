from piecetype import PieceType
from playingpiece import playingPiece

class PlayingpieceX(playingPiece):

    def __init__(self) -> None:
        super().__init__(PieceType.X)