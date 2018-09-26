from Card import Card
from Player import Player
from PlayerLogic.Simple import SimplePlayer
import constants
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
        self.wagers = {}
    
    def resetDeck(self, decks):
        self.pile = []
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
    
    def playGame(self):
        while len(self.players) > 0:
            self.playTurn()
        print "GAME OVER"

    def playTurn(self):
        self.wagers = {player: player.makeWager() for player in self.players}

        activePlayers = self.players[:]
        inactivePlayers = []
        for player in activePlayers:
            self.dealCard(player)
            self.dealCard(player)
        
        # giving cards to dealer
        self.dealCard(self.dealer)
        self.dealCard(self.dealer)

        # all players finish their hands first
        while len(activePlayers) > 0:
            currentPlayer = activePlayers.pop(0)
            currentPlayer.executeAction(self)
            if currentPlayer.isActive():
                activePlayers.append(currentPlayer)
            else:
                inactivePlayers.append(currentPlayer)
        
        # dealer finishes his hand
        while self.dealer.isActive():
            self.dealer.executeAction(self)
        
        # distribute earnings
        # TODO: account for 3:2 wager payouts, etc
        for player in inactivePlayers:
            playerHandValue = player.getHandValue()
            dealerHandValue = self.dealer.getHandValue()
            print player.name + ' hand: ' + str(player.hand) + ' | value: ' + str(playerHandValue)
            print 'dealer hand: ' + str(self.dealer.hand) + ' | value: ' + str(dealerHandValue)
            if playerHandValue <= 21:
                # player automatically loses their wager if they bust
                if dealerHandValue > 21 or playerHandValue > dealerHandValue:
                    print 'player ' + player.name + ' won!'
                    player.adjustBalance(self.wagers[player])
                elif dealerHandValue == playerHandValue:
                    print 'player ' + player.name + ' tied dealer!'
                    player.adjustBalance(0)
                else:
                    player.adjustBalance(-1*self.wagers[player])
                    print 'dealer won'
            else:
                player.adjustBalance(-1*self.wagers[player])
                print 'dealer won'

        for player in self.players:
            print player.money
            if player.isBroke():
                self.players.remove(player)

        # reset all players hands
        for player in self.players:
            player.resetHand()
        
        # reset dealers hand
        self.dealer.resetHand()

        # reset the deck
        self.resetDeck(self.deckNumber)
        
        self.wagers = {}