# BATTLESHIP-PYTHON


Summary - The object of Battleship is to try and sink all of the other player's before they sink all of your ships. All of the other player's ships are somewhere on his/her board.  You try and hit them by calling out the coordinates of one of the squares on the board.  The other player also tries to hit your ships by calling out coordinates.  Neither you nor the other player can see the other's board so you must try to guess where they are.  Each board in the physical game has two grids:  the lower (horizontal) section for the player's ships and the upper part (vertical during play) for recording the player's guesses.

Battleship can typically be played on a 10x10 board using ships of various lengths. These ships can either go horizontally or vertically.

The winner of the game is the person who can take out each player's ships first.



📝 `NOTE - This image was retrieved from wikipedia :`

## Mock Image
<img src="https://github.com/nahomebssa/battleship-python/blob/main/battleship_image.JPG" width=600><br>



## User Stories
### 1. Create a game board:

- [x] Create a game board that is at least 10x10 (Dimensions up to your team)
- [x] Draw board and make it visible to player 1 on their turn, and player 2 on theirs.
- [x] Each player will have their own board to target

### 2. Player Places ships:

- [x] Each player can place their ships either horizontally, or vertically on the board.
- [x] Each player is given their own turn to play their own ships

### 3. Toggle to the next player:

- [x] Each player can take turns attacking/guessing where the other players ship are, then alternates to the next player

### 4. Game Loop / Is Game Finished:

- [x] Have a loop of the game running while both players have their battleships alive
- [x] If one of the players battleships are all taken out, then they lose 

### 5. Player X attacks (Rows & Columns):

- [x] Player gets to put in a row/column for their attack / User Input
- [x] Check if valid hit and mark an X if it’s a hit, a 0 if it is a miss.
- [x] Update the board to represent how they performed

### 6. Game over check:

- [x] Perform a game over check 
- [x] Exit loop/end program

### 7. Required Ship Amount:

- [x] Have at least 2 different ship sizes (Length of 3, 4, 5, etc)
- [x] Have at least 4 ships.



## How to Interact with Game:

- Have appropriate libraries installed (unittest, os)
- Open file from terminal and run (python main.py) to start interacting with game.

📝 `NOTE - The Gif below doesn't show entire game as that's long for a gif (shows intial game stages) :`

<img src="https://github.com/nahomebssa/battleship-python/blob/main/buildingShips.gif" width=600><br>


### Challenges faced:

- Not all ships are sunk if more than one ships are placed on the board.


