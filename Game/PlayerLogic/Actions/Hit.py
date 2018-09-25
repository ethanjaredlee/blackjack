import IAction
import ipdb

class Hit(IAction.IAction):
    def legal(self, player, admin):
        return player.getHandValue() <= 21

    def effect(self, player, admin):
        # Admin deals a card to player
        admin.dealCard(player)
        if player.getHandValue() > 21:
            player.bust()

    def actionName(self):
        return "Hit"