from Card import Card
from Player import Player
import constants
import random

class Admin(object):

    def __init__(self, decks):
        assert decks > 0, "Number of decks must be greater than 0"

        self.deckNumber = decks
        self.pile = []
        for _ in range(decks):
            self.pile.extend([Card(rank, suit) for rank in constants.CARD_RANKS 
                                               for suit in constants.CARD_SUITS])

    def shuffle(self):
        assert len(self.pile) == self.deckNumber * 52, "Full deck is needed to shuffle"

        random.shuffle(self.pile)
    
    def addPlayers(self):
        name = raw_input("Enter player name")
        logic = "human"
        player = Player(logic, name)
        safe = "safe logic"
        dealer = Player(safe, "Dealer")