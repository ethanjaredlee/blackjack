import PlayerLogic.Actions.Hit as Hit
import PlayerLogic.Actions.Stand as Stand
import PlayerLogic.Actions.Double as Double 

ACTIONS = [
    Hit.Hit(),
    Stand.Stand(),
    Double.Double()
]

# Standard deck card ranks and suits
CARD_RANK_NUMBERS = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
CARD_RANK_FACES = ["J", "Q", "K"]
CARD_RANK_ACE = ["A"]
CARD_RANKS = CARD_RANK_NUMBERS + CARD_RANK_FACES + CARD_RANK_ACE
CARD_SUITS = ["Spade", "Diamond", "Club", "Heart"]
