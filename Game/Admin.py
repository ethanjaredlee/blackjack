from Card import Card
from Player import Player
from PlayerLogic.Simple import SimplePlayer
import constants
import PlayerLogic.Actions.Hit as Hit 
import random
import ipdb

class Admin(object):

    def __init__(self, decks):
        assert decks > 0, "Number of decks must be greater than 0"

        self.deckNumber = decks
        self.pile = []
        dealerLogic = SimplePlayer()
        self.resetDeck(decks)
        self.dealer = Player(dealerLogic, 'Dealer')
        self.players = []

        # initializing all the created actions
        self.actions = [
            Hit.Hit()
        ]
    
    def resetDeck(self, decks):
        for _ in range(decks):
            self.pile.extend([Card(rank, suit) for rank in constants.CARD_RANKS 
                                               for suit in constants.CARD_SUITS])
        self.shuffle()

    def addPlayer(self, player):
        self.players.append(player)

    def shuffle(self):
        assert len(self.pile) == self.deckNumber * 52, "Full deck is needed to shuffle"
        random.shuffle(self.pile)
    
    def dealCard(self, player):
        card = self.pile.pop()
        player.acceptCard(card)
    
    def givePlayerActions(self, player):
        legalActions = []
        for action in self.actions:
            if action.legal(player, self):
                pass
        pass
    
    def executePlayerAction(self, player, action):
        pass

    def playTurn(self):
        ipdb.set_trace()
        wagers = {player: player.makeWager() for player in self.players}

        activePlayers = self.players
        for player in activePlayers:
            self.dealCard(player)
            self.dealCard(player)
        
        # giving cards to dealer
        self.dealCard(self.dealer)
        self.dealCard(self.dealer)

        # all players finish their hands first
        while len(activePlayers) > 0:
            currentPlayer = activePlayers.pop(0)
            action = self.givePlayerActions(currentPlayer) 
            self.executePlayerAction(currentPlayer, action)
            if currentPlayer.isActive():
                activePlayers.append(player)
        
        # dealer finishes his hand
        while self.dealer.isActive():
            action = self.givePlayerActions(self.dealer)
            self.executePlayerAction(self.dealer, action)
        
        # distribute earnings
        for player in self.players:
            if player.getHandValue > self.dealer.getHandValue:
                player.awardEarnings(wagers[player])

        # reset all players hands
        for player in self.players:
            player.resetHand()
        
        # reset dealers hand
        self.dealer.resetHand()

        # reset the deck
        self.resetDeck(self.deckNumber)


            
        # each player makes their wager
        # deal hands
        # for all players that are active
        #   give them actions
        #   execute that action
        # distribute money
        # reset cards
        pass