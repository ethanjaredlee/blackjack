import constants
import ipdb

class Hand(object):
    def __init__(self):
        self.cards = []
    
    def __len__(self):
        return len(self.cards)
    
    def __repr__(self):
        return str(self.cards)
    
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

        # return the value closest to 21 with each ace being 1 or 11
        if aces > 0:
            possibleValues = []
            possibleValues.append(value + aces)
            for ace in range(aces):
                possibleValues.append(possibleValues[0] + 10*(ace+1))
            legalValues = [val for val in possibleValues if val <= 21]
            if len(legalValues) == 0:
                value = possibleValues[0]
            else:
                value = legalValues.pop()

        return value
