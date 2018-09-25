import IAction

class Double(IAction.IAction):
    def legal(self, player, admin):
        return player.cardCount() == 2 and player.isActive()
    
    def effect(self, player, admin):
        admin.dealCard(player)
        player.active = False
        admin.wagers[player] *= 2

    def actionName(self):
        return "Double"