# Boardgames
#Required Files

**driver.py**

Contain a main function

**executive.py**

Contain an Executive class

Handle file I/O and user interaction

Creates a list of board games by extracting the information from file

**boardgame.py**

Contain a BoardGame class


#File format

The file contains several rows, each row contains the information for a single game.

Each game has the following information name gibbonsrating baverage avgweight yearpublished bggbestplayers All data here has been provided by Board Game Geek

**name**: name of the game

**gibbonsrating**: my rating of the game

**baverage**: average rating on board game geek

**avgweight**: the complexity of the game as voted on by the public; ranges from 0 to 5, 5 being the most complex

**yearpublished**: year it was published

**bggbestplayers**: best player count (for example, sometimes a game that plays 2-6 players is most fun at 4 or 5)

#User's Menu

-**Print all games highest Gibbons rating to lowest**

-**Print all games from a year**
Obtain a year from the user and either print all the games from that year or print "No games found"

-**Print all games with a weight equal to or lower than a provided weight**
Obtain a weight (e.g. 0-5) from the user and print all games at or below that weight

-**The People VS Dr. Gibbons**
The goal of this is see where Dr. Gibbons and the people disagree
Obtain a number (0-10, decimals allowed) from the user and print all games where the people's rating and Dr. Gibbons rating are separated by that much or more
Example, if the user wanted to see all games where the people's rating and Dr. Gibbons' rating differed by more than 1.5, they would enter 1.5 at the prompt then you see games where my rating and the bggrating differ by 1.5 or more.
NOTE: This option doesn't care which rating is higher, it just prints games where ratings differ by a threshold set by the user

-**Print based on player count**
Obtain a player count
Print all games that are best at the count

-**Exit the program**
