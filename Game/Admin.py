from Card import Card
from Player import Player
from PlayerLogic.Simple import SimplePlayer
import constants
import random

class Admin(object):

    def __init__(self, decks):
        assert decks > 0, "Number of decks must be greater than 0"

        self.deckNumber = decks
        self.pile = []
        for _ in range(decks):
            self.pile.extend([Card(rank, suit) for rank in constants.CARD_RANKS 
                                               for suit in constants.CARD_SUITS])
        dealerLogic = SimplePlayer()
        self.players = [Player(dealerLogic, 'Dealer', True)]
    
    def addPlayer(self, player):
        self.players.append(player)

    def shuffle(self):
        assert len(self.pile) == self.deckNumber * 52, "Full deck is needed to shuffle"
        random.shuffle(self.pile)
    
    def dealCard(self, player):
        card = self.pile.pop()
        player.acceptCard(card)
    
    def acceptWagers(self):
        return {player: player.makeWager() for player in self.players if not player.dealer}

    def givePlayerActions(self):
        pass

    def playTurn(self):
        pass