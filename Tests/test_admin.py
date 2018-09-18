import Game.Admin as Admin
import unittest

class AdminTestCase(unittest.TestCase):
    def test_deck_construction(self):
        # Test deck construction of unique cards
        admin = Admin.Admin(3)
        self.assertEqual(len(set(admin.pile)), 52*3)