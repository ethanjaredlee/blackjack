from Hand import Hand
from PlayerLogic.IPlayerLogic import IPlayer

class Player(object):
    def __init__(self, playerLogic, name, dealer=False):
        self.iplayer = playerLogic
        self.name = name
        self.hand = Hand()
        self.money = 1000
        self.dealer = dealer

    def acceptCard(self, card):
        self.hand.addCard(card)

    def getHandValue(self):
        return self.hand.getValue()

    def makeWager(self):
        return self.iplayer.makeWager(self.money)
