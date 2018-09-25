# blackjack

## Thought Process
Making the game blackjack doesn't seem like too hard of a task at first. However, blackjack comes with a lot of little nuances that I don't want to worry about right now, but I might want to add in in the future. An example of this is actions that are available to a player. At first I thought blackjack was played with just hit and stand rules, but quickly found out that there are other actions like doubling and insurance. The challenge I wanted to add in this code was to make it robust and easily modified if I wanted to include more actions or features in the future. 

## Game Limitations
Right now, the game has 3 actions: Hit, Double, or Stand. This is enough for a human player to play a full game (if I had a human player implemented). Currently, I've been playing the game with two dummy players, the dealer and another player. 

## Game Design Choices
Each player has it's own player logic that implements the ABC IPlayerLogic.py. This way we can do cool things like implement different player AIs, a human interface, or even create a player that can communicate over a network (I did this in a Tsuro board game implementation). 
An individual action can also be added, it just has to implement IAction, defining prerequisites for the action to be implemented and what the action actually does. 

## Shortcomings
* Testing. I was running out of time and haven't written that many unit tests
* As much as I wanted to make this game modular, and have the ability to have third parties add in actions, I'm passing in the game administrator which isn't very safe because it allows an action to change how the game is being played completely. Thinking about the real world, this seems fine however, because different actions do change how the game is being played and almost allows rules to be redefined. 
