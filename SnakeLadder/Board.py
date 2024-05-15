from Cell import Cell
from random import randint
from Cell import Cell
from Jump import Jump
from JumpType import JumpType
class Board:

    def __init__(self, size, noOfSnake, noOfLadder) -> None:
        self.size = size
        self.noOfSnake = noOfSnake
        self.noOfLadder = noOfLadder
        self.cells = [[Cell() for i in range(size)] for i in range(size)]
        self.initializeLadders()
        self.initializeSnakes()

    def getCell(self, diceVal):

        row = diceVal // self.size
        if row >= self.size:
            return None
        col = diceVal % self.size
        cell = self.cells[row][col]
        updatedCell = self.checkForJump(cell)
        return updatedCell

    def checkForJump(self, cell):
        updatedCell = cell
        if cell.jump is not None:
            end = cell.jump.end
            newRow = end // self.size
            newCol = end % self.size
            updatedCell = self.board[newRow][newCol]
        return updatedCell
        
    
    def initializeSnakes(self):
        snakeAdded = 0
        while snakeAdded < self.noOfSnake:
            start = randint(0, self.size * self.size - 1)
            end = randint(0,start)
            if start == end:
                continue
            cell = self.getCell(start)
            snake = Jump(start, end, JumpType.SNAKE)
            if cell.jump is not None:
                continue
            cell.jump = snake
            snakeAdded += 1

    def initializeLadders(self):
        ladderAdded = 0
        while ladderAdded < self.noOfLadder:
            end = randint(0, self.size * self.size - 1)
            start = randint(0,end)
            if start == end:
                continue
            cell = self.getCell(start)
            ladder = Jump(start, end, JumpType.LADDER)
            if cell.jump is not None:
                continue
            cell.jump = ladder
            ladderAdded += 1
                
