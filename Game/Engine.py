import Admin
import Player
import PlayerLogic.Simple as Simple
import PlayerLogic.Human as Human

if __name__ == "__main__":
    admin = Admin.Admin(4)
    player = Player.Player(Human.HumanPlayer(), "Ethan")
    admin.addPlayer(player)
    admin.playTurn()