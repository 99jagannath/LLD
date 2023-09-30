
class Board:

    def __init__(self) -> None:
        self.board_map = [[None for i in range(3)] for j in range(3)]

    def getBoardMap(self):
        return self.board_map

    def getEmptySpace(self):
        empty_list = []
        for i in range(3):
            for j in range(3):
                if self.board_map[i][j] is None:
                    empty_list.append((i,j))
        return empty_list
    
    def addEntry(self, row, column, playingPiece):
        if self.board_map[row - 1][column - 1] is not None:
            print("Invalid move.....! Some other value is already there")
            return False
        self.board_map[row - 1][column - 1] = playingPiece.pieceType
        return True
        
        
    def printBoard(self):
        for i in range(3):
            for j in range(3):
                print(self.board_map[i][j], end=" ")
            print("\n")
        