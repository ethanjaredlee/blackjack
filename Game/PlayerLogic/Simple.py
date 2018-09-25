from IPlayerLogic import IPlayer
import constants
import Actions as Actions
import ipdb

class SimplePlayer(IPlayer):
    """ 
    Simple logic that hits on every hand when the value is less than 17
    """
    def __init__(self):
        pass

    def chooseAction(self, hand, admin, legalActions):
        if any(isinstance(action, Actions.Hit.Hit) for action in legalActions):
            return Actions.Hit.Hit()
        else:
            print "hit not found"
            return None
    
    def makeWager(self, remaining):
        return 10