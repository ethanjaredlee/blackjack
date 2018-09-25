from IPlayerLogic import IPlayer
import constants
import Actions.Hit as Hit
import Actions.Stand as Stand
import Actions.Double as Double
import ipdb

class SimplePlayer(IPlayer):
    """ 
    Simple logic that hits on every hand when the value is less than 17,
    otherwise the player stands
    """
    def __init__(self):
        pass

    def chooseAction(self, hand, admin, legalActions):
        if hand.getValue() < 17 and any(isinstance(action, Hit.Hit) for action in legalActions):
            return Hit.Hit()
        else:
            return Stand.Stand()
    
    def makeWager(self, remaining):
        return 10