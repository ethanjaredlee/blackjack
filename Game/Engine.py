import Admin
import Player
import PlayerLogic.Simple as Simple

if __name__ == "__main__":
    admin = Admin.Admin(4)
    player = Player.Player(Simple.SimplePlayer(), "Ethan")
    admin.addPlayer(player)
    admin.playTurn()