from Hand import Hand
from PlayerLogic.IPlayerLogic import IPlayer

class Player(object):
    def __init__(self, playerLogic, name):
        self.iplayer = playerLogic
        self.name = name
        self.hand = Hand()
        self.money = 1000
        self.active = True

    def acceptCard(self, card):
        self.hand.addCard(card)

    def getHandValue(self):
        return self.hand.getValue()

    def makeWager(self):
        wager = self.iplayer.makeWager(self.money)
        self.money -= wager
        return wager

    def isActive(self):
        return self.active
    
    def awardEarnings(self, wager):
        self.money += wager*2               # 2x because player is paid wager back
    
    def resetHand(self):
        self.hand = Hand()