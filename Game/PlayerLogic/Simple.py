from IPlayerLogic import IPlayer

class SimplePlayer(IPlayer):
    """ 
    Simple logic that hits on every hand when the value is less than 17
    """
    def __init__(self):
        pass

    def chooseAction(self, hand):
        if hand.getValue() < 17:
            # then hit
            pass
        return 1