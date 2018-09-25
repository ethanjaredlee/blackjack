from Hand import Hand
from PlayerLogic.IPlayerLogic import IPlayer
import constants

class Player(object):
    def __init__(self, playerLogic, name):
        self.iplayer = playerLogic
        self.name = name
        self.hand = Hand()
        self.money = 1000
        self.active = True

    def acceptCard(self, card):
        self.hand.addCard(card)
    
    def bust(self):
        self.active = False

    def getHandValue(self):
        value = self.hand.getValue()
        if value > 21:
            self.bust()
        return value

    def makeWager(self):
        wager = self.iplayer.makeWager(self.money)
        self.money -= wager
        return wager

    def isActive(self):
        return self.active
    
    def awardEarnings(self, wager):
        self.money += wager*2               # 2x because player is paid wager back
    
    def returnWager(self, wager):
        self.money += wager
    
    def resetHand(self):
        self.hand = Hand()

    def executeAction(self, admin):
        legalActions = []
        for action in constants.ACTIONS:
            if action.legal(self, admin):
                legalActions.append(action)
        action = self.iplayer.chooseAction(self.hand, admin, legalActions)
        action.effect(self, admin)