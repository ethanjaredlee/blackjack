import constants

class Card(object):
    """ 
    Class representing a single card
    """
    def __init__(self, rank, suit):
        # check rank is value
        assert rank in constants.CARD_RANKS
        assert suit in constants.CARD_SUITS

        self.rank = rank
        self.suit = suit
  
    def __repr__(self):
        return "[" + self.rank + "|" + self.suit + "]"

    def getValue(self, player):
        if self.rank in [str(n) for n in range(2,11)]:
            # number card
            return self.rank
        elif self.rank in ["J", "Q", "K"]:
            # face card
            return 10
        elif self.rank == "A":
            # ace card
            if player.score > 10:
                return 1
            else:
                return 11
        else:
            # none of the above
            raise ValueError("Card rank is not a standard 2-10, J, Q, K, or A value")
        