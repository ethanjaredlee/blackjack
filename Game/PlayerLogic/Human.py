from IPlayerLogic import IPlayer

class HumanPlayer(IPlayer):
    def __init__(self):
        pass

    def chooseAction(self, hand, admin, legalActions):
        for action in legalActions:
            print action.actionName
        return 1
    
    def makeWager(self, remaining):
        return 1