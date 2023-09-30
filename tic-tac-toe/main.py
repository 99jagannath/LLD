from player import Player
from game import Game
from board import Board
from playingpieceO import PlayingpieceO
from playingpieceX import PlayingpieceX

def main():
    player1 = Player("A", PlayingpieceX())
    player2 = Player("B", PlayingpieceO())
    game = Game(Board())

    game.registerPlayer(player1)
    game.registerPlayer(player2)
    game.startGame()

if __name__ in ['main', '__main__']:
    main()