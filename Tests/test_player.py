import Game.Player as Player
import Game.PlayerLogic.Human as Human
import Game.PlayerLogic.IPlayerLogic as IPlayer
import unittest

class PlayerTestCase(unittest.TestCase):
    def test_player_construction(self):
        humanPlayer = Human.HumanPlayer()
        player = Player.Player(humanPlayer, "Ethan")
        self.assertEquals(player.name, "Ethan")