import Game.Card as Card
import Game.constants as constants
import unittest

class CardTestCase(unittest.TestCase):
    def test_card_construction(self):
        for rank in constants.CARD_RANKS:
            for suit in constants.CARD_SUITS:
                card = Card.Card(rank, suit)
                self.assertEqual(card.rank, rank)
                self.assertEqual(card.suit, suit)

    def test_bad_rank(self):
        with self.assertRaises(AssertionError):
            Card.Card(1, "Spade")

    def test_bad_suit(self):
        with self.assertRaises(AssertionError):
            Card.Card(2, "Joker")

if __name__ == "__main__":
    unittest.main()
