from Game.Card import Card
import unittest

class CardTestCase(unittest.TestCase):
    def test_card_construction(self):
        card = Card("J", "Spade")
        self.assertEqual(card.rank, "J")

if __name__ == "__main__":
    unittest.main()
