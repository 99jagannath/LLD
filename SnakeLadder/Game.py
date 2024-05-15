from Board import Board
from Dice import Dice
from collections import deque
from User import User
from RedPiece import RedPiece
from GreenPiece import GreenPiece

class Game:
    def __init__(self):
        self.boardSize = 10
        self.noOfLadder = 5
        self.noOfSnake = 5
        self.noOfDice = 2
        self.noOfUser = 2
        self.board = Board(self.boardSize, self.noOfLadder, self.noOfSnake)
        self.dice = Dice(self.noOfDice)
        self.users = deque()
        self.initialiseUser()

    
    def initialiseUser(self):
        for _ in range(self.noOfUser):
            user = User(1, "Jagan", RedPiece())
            self.users.append(user)

    def findWinner(self):
        if self.board[0][self.boardSize - 1].User is not None:
            return self.board[0][self.boardSize - 1].User
        return None
    
    def startGame(self):
        while True: # game loop
            print("\n\n")
            print("------------------------------")
            user = self.users.popleft()
            diceRolls = self.dice.rollDices()
            cell = self.board.getCell(diceRolls)
            if cell is None:
                self.users.append(user)
                print("InvalidInput")
                continue
            cell.user = user
            winner = self.findWinner()
            if winner is not None:
                print("Winner is %s" % user.name)
                break
            self.users.append(user)


    


