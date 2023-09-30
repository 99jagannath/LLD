class Game:
    def __init__(self, board) -> None:
        self.board = board
        self.players = []

    def registerPlayer(self, player):
        self.players.append(player)

    @staticmethod
    def validate_input(player_input):
        row, column = player_input.split(',')
        row = int(row)
        column = int(column)
        if row < 1 and row > 3:
            return False, row, column
        else:
            return True, row, column

    def startGame(self):
        print("Game has been started....")
        finishGame = False

        while not finishGame:
            if len(self.players) < 2:
                print("Please register more players before starting game")
            player = self.players[0]
            print("Turn - %s" % player.getName())
            player_input = input("Please enter the input \"[1-3],[1-3]\"")
            validInput, row, column = Game.validate_input(player_input)
            if not validInput:
                print("Please Enter valid input[1-3][1-3]")
                continue
            pieceAdded = self.board.addEntry(row, column, player.getPieceType())
            if not pieceAdded:
                continue
            self.board.printBoard()
            self.players.pop(0)
            self.players.append(player)
            if Game.isThereAnyWinner(row, column, player.getPieceType(), self.board.getBoardMap()):
                print("Winner is player %s" % player.getName())
                break
            emptySpace = self.board.getEmptySpace()
            if len(emptySpace)  == 0:
                print("Math is drawn.....")
                finishGame = True

    @staticmethod
    def isThereAnyWinner(row, column, pieceType, board):
        vertical_match = True
        for i in range(3):
            if board[row - 1][i] != pieceType.pieceType:
                vertical_match = False
                break

        horizontal_match = True
        for i in range(3):
            if board[i][column - 1] != pieceType.pieceType:
                horizontal_match = False
                break

        left_diagonal_match = True
        for i in range(3):
            if board[i][i] != pieceType.pieceType:
                left_diagonal_match = False
                break

        right_diagonal_match = True
        for i in range(3):
            if board[2 - i][i] != pieceType.pieceType:
                right_diagonal_match = False
                break
        return vertical_match or horizontal_match or left_diagonal_match or right_diagonal_match



