import Game.PlayerLogic.Actions as Actions
import Game.Admin as Admin
import Game.Player as Player
import Game.PlayerLogic.Simple as Simple
import unittest

class ActionsTestCase(unittest.TestCase):
    def setUp(self):
        self.NUMBER_OF_DECKS = 4
        self.admin = Admin.Admin(self.NUMBER_OF_DECKS)
        simpleLogic = Simple.SimplePlayer()
        self.player = Player.Player(simpleLogic, "Ethan")

    def test_hit(self):
        pass