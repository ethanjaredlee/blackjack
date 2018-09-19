import IAction

class Hit(IAction.IAction):
    def legal(self, player, dealer):
        return player.getHandValue() <= 21

    def effect(self, player, dealer):
        # Dealer deals a card to player
        pass
