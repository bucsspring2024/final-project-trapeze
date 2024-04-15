[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14587024&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Project Title >>
## CS110 Final Project  << Semester, Year >>

## Team Members

Layla Shihada

***

## Project Description

Right now, I'm considering a matching/memory game. There are a certain number of tiles that the player has to click on to flip over. The user clicks a tile to turn it over, and clicks a second one to find its match. On the main screen, the player can select the time limit and how many pairs of tiles they want to match (i.e., 4 pairs, 5 pairs, 6 pairs); they gain points for each game won based on increasing difficulty. If the player fails to match a pair of tiles 3 times, then the game is over.  

***    

## GUI Design

### Initial Design

![initial gui](file:///Users/laylashihada/Downloads/GUI_CS110.pdf)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Start menu (Select the difficulty/number of tiles)
2. How to play screen
3. Scoreboard
4. Mistake tracker
5. Game over screen
6. Timer

### Classes

class Tile:
    
    def __init__(self, symbol):
        """
        Initialize a tile with a symbol and a status of being hidden.
        """
        self.symbol = symbol
        self.is_hidden = True

    def reveal(self):
        """
        Reveal the symbol on the tile.
        args: None
        """
        pass

    def hide(self):
        """
        Hide the symbol on the tile.
        args: None
        """
        pass

    def is_match(self, other_tile):
        """
        Check if this tile matches with another tile.
        args: other_tile (Tile)
        """
        pass

class Scoreboard:
    
    def __init__(self):
        """
        Initialize a scoreboard with a score of 0.
        args: None
        """
        self.score = 0

    def increment_score(self):
        """
        Increment the score by 10 points.
        args: None
        """
        pass

    def reset_score(self):
        """
        Reset the score to 0.
        args: None
        """
        pass

    def display_score(self):
        """
        Display the current score.
        args: None
        """
        pass
 

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
