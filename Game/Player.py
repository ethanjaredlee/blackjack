class Player(object):
    def __init__(self, playerLogic, name):
        self.iplayer = playerLogic
        self.name = name
        self.hand = []

    def acceptCard(self, card):
        self.hand.append(card)