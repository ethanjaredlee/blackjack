import constants

class Card(object):
    """ 
    Class representing a single card
    Note: Cards do not have intrinsic values, hands do
    """
    def __init__(self, rank, suit):
        assert rank in constants.CARD_RANKS, "Rank does not exist"
        assert suit in constants.CARD_SUITS, "Suit does not exist"

        self.rank = rank
        self.suit = suit
  
    def __repr__(self):
        return "[" + self.rank + "|" + self.suit + "]"
