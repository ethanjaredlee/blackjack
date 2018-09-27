# blackjack

## Running the game/tests
To start the game from the root directory, run `python Game/Engine.py`
To run tests from the root directory, run `python -m unittest discover`

## Rules
Single player blackjack game with the ability to hit, stand, and double. Payouts are always 1:1 and there is no insurance. 

## Design
This code was designed for continued development outside the scope of the original project. The current stage for this would be considered an MVP.
* Admin handles the logic of playing each turn and keeps track of each player and the deck
* Player holds information about their hand, money, logic and whether they're still active in the current turn. I abstracted the player logic so that you can add other players to the game that implement different strategies, human players, and even networked players. 
* IAction is an interface to allow a future developer (myself) to add more actions like insurance and a blackjack 3:2 payout. I made it like this because I knew I wouldn't have the proper time to implement all the actions in blackjack. 
* Hand holds cards and can calculate the total value of the cards it carries. Fairly straightforward stuff except aces can be 1 or 11 and will yield the value of the hand less than or closest to 21. 

## Tooling
I used pretty basic tools. I was originally going to choose C# as my language because it's a strongly typed language, but I already finished a project like this in C# and wanted to try it in Python. Also Python development is "faster". I used the basic unittest library and ipdb as my debugger.

## Shortcomings
* My tests suck to be honest. I'm working on getting more in there, but wanted to submit my code asap
* I could include more contracts
* I need a couple more actions for this to be a complete game
* GUI interface
* Multiplayer 

## Reflection
I probably could've finished this project in a quarter of the time if I just hacked my way through it. However I wanted to try making it in such a way that was cleaner and more extensible (what if someone's playing a variation of blackjack and wanted to modify the code for that). I have to learn to get better at writing tests quickly, scratch that, writing **good tests** quickly. I had this bug where hand value wasn't being calculated correctly and my tests still passed. 

TL;DR: thanks for the challenge, I learned a lot and would love any feedback if you're allowed to give it because I know someone out there is cringing at my code quality. 