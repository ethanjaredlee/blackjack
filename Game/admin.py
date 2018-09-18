from Card import Card
import constants

class Admin(object):

    def __init__(self, decks):
        assert decks > 0, "Number of decks must be greater than 0"

        self.pile = []
        for _ in range(decks):
            self.pile.extend([Card(rank, suit) for rank in constants.CARD_RANKS for suit in constants.CARD_SUITS])