import Game.Hand as Hand
import Game.Card as Card
import unittest

class HandTestCase(unittest.TestCase):
    def test_hand(self):
        hand = Hand.Hand()
        hand.addCard(Card.Card("K", "Spade"))
        hand.addCard(Card.Card("3", "Spade"))
        self.assertEquals(hand.getValue(), 13)

    def test_hand_ace(self):
        hand = Hand.Hand()
        hand.addCard(Card.Card("A", "Spade"))
        hand.addCard(Card.Card("A", "Spade"))
        hand.addCard(Card.Card("A", "Spade"))
        self.assertEquals(hand.getValue(), 13)

    def test_hand_ace_bust(self):
        hand = Hand.Hand()
        hand.addCard(Card.Card("A", "Spade"))
        hand.addCard(Card.Card("3", "Spade"))
        hand.addCard(Card.Card("K", "Spade"))
        hand.addCard(Card.Card("K", "Spade"))
        self.assertEquals(hand.getValue(), -1)
    
    def test_hand_ace_extreme(self):
        hand = Hand.Hand()
        for _ in range(21):
            hand.addCard(Card.Card("A", "Spade"))
        self.assertEquals(hand.getValue(), 21) 