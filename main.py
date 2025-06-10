from utils.game import Board
from utils.player import Player
from utils.player import Deck


# Launch the game

names = ["John", "Ana", "Rob","Sofia"]

cards_per_player = 52 / len(names)

# Start the first game

game = Board(names)
game.start_game()


    