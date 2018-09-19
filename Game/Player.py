from Hand import Hand
from PlayerLogic.IPlayerLogic import IPlayer

class Player(object):
    def __init__(self, playerLogic, name):
        self.iplayer = playerLogic
        self.name = name
        self.hand = Hand()

    def acceptCard(self, card):
        self.hand.addCard(card)

    def getHandValue(self):
        return self.hand.getValue()