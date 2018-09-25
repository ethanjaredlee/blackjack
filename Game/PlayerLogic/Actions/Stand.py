import IAction

class Stand(IAction.IAction):
    def legal(self, player, admin):
        return True
    
    def effect(self, player, admin):
        player.active = False

    def actionName(self):
        return "Stand"