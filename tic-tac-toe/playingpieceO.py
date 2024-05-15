from piecetype import PieceType
from playingpiece import playingPiece


class PlayingpieceO(playingPiece):

    def __init__(self) -> None:
        super().__init__(PieceType.O)