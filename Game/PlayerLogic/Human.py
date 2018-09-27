from IPlayerLogic import IPlayer

class HumanPlayer(IPlayer):
    def __init__(self):
        pass

    def chooseAction(self, hand, admin, legalActions):
        print ''

        print 'Your hand: ' + str(hand) + ' | value: ' + str(hand.getValue())
        print "Dealers face-up card: " + str(admin.dealer.hand.cards[0]) 

        print ''

        for i, action in enumerate(legalActions):
            print str(i) + '. ' + action.actionName()

        actionIndex = int(raw_input('Choose the number of the action you want to take: '))
        return legalActions[actionIndex]
        
    
    def makeWager(self, remaining):
        wager = int(raw_input("How much do you wish to bet? "))

        return wager