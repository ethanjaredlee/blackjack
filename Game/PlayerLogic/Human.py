from IPlayerLogic import IPlayer

class HumanPlayer(IPlayer):
    def __init__(self):
        pass

    def chooseAction(self, hand):
        return 1
    
    def makeWager(self, remaining):
        return 1