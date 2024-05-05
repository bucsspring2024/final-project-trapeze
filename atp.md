# My Final Project

## ATP

### Test Case 1: Screen Navigation

- **Test Description:** Ensure that each button leads to the appropriate screen when clicked.
- **Steps:**
    1. Go to project folder, run ``main.py`` file to launch Pygame window
    2. Verify that program opens to "Menu" screen.
    3. Select the game's level of difficulty by clicking on the corresponding button.
    4. Verify that Pygame window displays the correct game screen. 
    5. After game is over, click "Back to Menu"
    6. Verify that Pygame window displays the "Menu" screen
- **Expected Outcome:**
    - Each button should direct the user to its corresponding screen when clicked:
        - *LEVEL 1:* Screen should display a "Level 1" heading, along with 8 blank tiles in 2 rows of 4. The "Moves Counter:" should be positioned under the tiles, updating the number of moves it takes to match all the tiles. 
        - *LEVEL 2:* Screen should display a "Level 2" heading, along with 16 blank tiles in 4 rows of 4. The "Moves Counter:" should be positioned under the tiles, updating the number of moves it takes to match all the tiles.
        - *LEVEL 3:* Screen should display a "Level 3" heading, along with 24 blank tiles in 4 rows of 6. The "Moves Counter:" should be positioned under the tiles, updating the number of moves it takes to match all the tiles.
        - *BACK TO MENU:* Screen should display the main menu, which includes 3 buttons that describe each level of the game. Clicking this button on the "Game Over" screen directs the user back to the beginning of the game sequence so they can keep playing.

### Test Case 2: Color Visibility

- **Test Description:** Verify that colors of tiles are hidden/unhidden according to game events and user interaction.
- **Steps:**
    1. Go to project folder, run ``main.py`` file to launch Pygame window
    2. Select a level of difficulty from Main Menu
    3. Before starting the game, verify that the tiles' colors are hidden 
    4. Click a tile
    5. Verify that this tile's color is revealed and remains visible
    6. Click a second tile
    7. Verify that the second tile's color is revealed. 
    8. If the tiles match, verify that their colors remain visible. If the tiles do NOT match, verify that the colors are re-hidden.
- **Expected Outcome:** Colors should be hidden when game starts and clicking a tile should reveal its color. If the second tile matches the first, their colors remain visible. If not, the colors are re-hidden.

### Test Case 3: Moves Counter

- **Test Description:** Make sure that the "Moves Counter" updates whenever a tile is clicked.
- **Steps:**
    1. Go to project folder, run ``main.py`` file to launch Pygame window
    2. Select a level of difficulty from Main Menu
    3. Verify that the "Moves Counter" starts at zero before game starts
    4. Click a tile to reveal its color
    5. Verify that the "Moves Counter" increases by 1
    6. Continue playing until all tiles are matched
    7. Verify that the "Moves Counter" stops updating when all the tiles are matched
- **Expected Outcome:** The "Moves Counter" should start at zero and increase by 1 every time a tile is clicked until the game is over.

### Test Case 4: Calculating Accuracy

- **Test Description:** Verify that "Accuracy" is calculated and displayed properly when a game ends.
- **Steps:** 
    1. Go to project folder, run ``main.py`` file to launch Pygame window
    2. Select a level of difficulty from Main Menu
    3. Determine the minimum number of moves required to match all the tiles. 
        - Level 1 = 8 moves
        - Level 2 = 16 moves
        - Level 3 = 24 moves
    4. Play game until all tiles are matched
    5. Verify that the "Moves Counter" accurately reflects the number of moves you made (i.e. number of times you clicked the tiles) to find all the matching colors
    6. Calculate your tile-matching Accuracy by dividing the minimum number of moves (depending on the level you're playing) by the number of moves you actually made during the game. Multiply that value by 100 to get a percentage. 
    7. Verify that the "Game Over" screen displays the correct Accuracy percentage 
- **Expected Outcome:** If the user matches all the tiles together in the minimum amount of moves, they have 100% accuracy. Otherwise, the "Game Over" screen should display their percentage accuracy by calculating as follows: (minimum number of moves / total number of moves) * 100

### Test Case 5: Match Detection
- **Test Description:** Ensure that tiles properly respond to mouse clicks/user interaction.
- **Steps:** 
    1. Go to project folder, run ``main.py`` file to launch Pygame window
    2. Select a level of difficulty from Main Menu
    3. Verify that colors are hidden for all tiles
    4. Start game by clicking on tile
    5. Verify that tile's color becomes visible when clicked on
    6. Click on second tile
    7. Verify that second tile's color becomes visible when clicked on
    8. Determine whether the second tile's color matches that of the first
    9. Verify that if the tiles match, their colors remain visible and the tiles' borders turns black
- **Expected Outcome:** If two tiles are matched together, their colors will no longer be hidden and the tiles' borders turn black to denote a correct match.
