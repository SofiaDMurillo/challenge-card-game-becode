from utils.player import Player
from utils.player import Deck

# Create a class BOARD with attributes: player, turn_count, active_cards,history_cards
    # Method start_game that will Start the game, Fill a Deck, Distribute the cards of the Deck to the players.
    # Make each Player play() a Card, where each player should only play 1 card per turn, and all players have to play at each turn until they have no cards left.

class Board():

    def __init__(self, names):
        self.players = []
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []
        for name in names:
            self.players.append(Player(name))
            

    def start_game(self):
        deck = Deck()
        deck.fill_deck()
        deck.shuffle()
        deck.distribute(self.players)

  


        
