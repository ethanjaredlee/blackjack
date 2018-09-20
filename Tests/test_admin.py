import Game.Admin as Admin
import Game.Player as Player
import Game.PlayerLogic.Simple as Simple
import unittest
import ipdb

class AdminTestCase(unittest.TestCase):
    def setUp(self):
        self.NUMBER_OF_DECKS = 4
        self.admin = Admin.Admin(self.NUMBER_OF_DECKS)
        simpleLogic = Simple.SimplePlayer()
        self.player = Player.Player(simpleLogic, "Ethan")

    def test_deck_construction(self):
        # Test deck construction of unique cards
        admin = Admin.Admin(3)
        self.assertEqual(len(set(admin.pile)), 52*3)

    def test_deal_card(self):

        self.assertEquals(len(self.player.hand), 0)
        self.assertEquals(len(self.admin.pile), 52*self.NUMBER_OF_DECKS)
        self.admin.dealCard(self.player)

        self.assertEquals(len(self.player.hand), 1)
        self.assertEquals(len(self.admin.pile), 52*self.NUMBER_OF_DECKS-1)
    
    def test_accept_wagers(self):
        self.admin.addPlayer(self.player)
        wagers = self.admin.acceptWagers()
        self.assertEquals(len(wagers), 1)
        self.assertEquals(wagers[self.player], 10)