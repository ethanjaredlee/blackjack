import Game.Dealer as Dealer
import unittest

class DealerTestCase(unittest.TestCase):
    def test_deck_construction(self):
        # Test deck construction of unique cards
        dealer = Dealer.Dealer(3)
        self.assertEqual(len(set(dealer.pile)), 52*3)