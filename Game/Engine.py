import Admin
import Player
import PlayerLogic.Simple as Simple
import PlayerLogic.Human as Human

if __name__ == "__main__":
    # initialization stuff
    while True:
        try:
            decks = int(raw_input("How many decks would you like to play with? "))
        except ValueError:
            print "Please enter a valid number"
        else:
            break
    
    admin = Admin.Admin(decks)
    player = Player.Player(Human.HumanPlayer(), "Ethan")
    admin.addPlayer(player)
    
    admin.playGame()