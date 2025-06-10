from utils.card import Card
import random

# Create a class Player with attributes: cards, turn_count, number_of_cards, history
class Player():

    def __init__(self, number_of_cards=0, history=None):
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = number_of_cards
        self.history = []

# Methods play () will pick a card, add to the history, print player choice, return the card
    def get_cards(self, player_cards):
        self.cards = player_cards


    def play (self):
        if len(self.cards)>0:            
            active_card = random.choice(self.cards)
            self.turn_count +=1
            self.number_of_cards = len(self.cards)
            self.history.append(active_card)
            print(f"Player played {active_card} (Turn {self.turn_count})")
            return active_card
        else:
            print("No cards left to play")

# Create a DECK class with attribute cards 

class Deck():

    def __init__(self):
        self.deck_cards = []

    def fill_deck(self):
        self.deck_cards= [Card(icon, value) for icon in icons for value in values]

    def shuffle(self):
        random.shuffle(self.deck_cards)

    def distribute(self,players):
        cards_per_player = len(self.deck_cards) // len(players)
    
        split = [self.deck_cards[i:i+1] for i in range (0, len(self.deck_cards), cards_per_player)]
        
        for player in players:
            for set in split:
                player.get_cards(set)


icons = ["♥", "♦", "♣", "♠"]
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']




