import constants
import ipdb

class Hand(object):
    def __init__(self):
        self.cards = []
    
    def __len__(self):
        return len(self.cards)
    
    def addCard(self, card):
        self.cards.append(card)

    def getValue(self):
        value = 0
        aces = 0
        for card in self.cards:
            if card.rank in constants.CARD_RANK_NUMBERS:
                value += int(card.rank)
            elif card.rank in constants.CARD_RANK_FACES:
                value += 10
            else:
                aces += 1
        if aces > 0:
            possibleValues = []
            for i in range(aces):
                possibleValues.append(value + (i+1)*1 + 11*(aces-i-1))
            possibleValues.sort()
            for i, val in enumerate(possibleValues):
                if val > 21:
                    value = possibleValues[max(0, i-1)]
                    break
        return value
