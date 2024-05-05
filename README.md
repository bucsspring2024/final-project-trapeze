[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14587024&assignment_repo_type=AssignmentRepo)


# Match Mania!
## CS110 - Final Project Spring 2024

## Team Members

Layla Shihada

***

## Project Description

My program runs a Tile Matching game. The user can select their preferred level of difficulty on the Main Menu, which will determine how many tiles they will have to match. From there, they'll be directed to a game screen that displays a grid of blank tiles. Each tile is assigned an invisible symbol that matches with one other tile on the grid, so the user must find the matching pairs by clicking on the tiles to reveal their symbols one at a time.

***    

## Additional Modules
- random (Reference Link: https://docs.python.org/3/library/random.html)
- re (Reference Link: https://docs.python.org/3/library/re.html)
- requests (API Link: https://github.com/cheatsnake/xColors-api?tab=readme-ov-file)


## GUI Design

### Initial Design

![initial gui](file:///Users/laylashihada/Downloads/GUI_CS110.pdf)

### Final Design
![Main Menu](main_menu.png)
![Level 1](level_1.png)
![Level 2](level_2.png)
![Level 3](level_3.png)
![Game Over](game_over.png)
## Program Design

### Features

1. Starting menu screen (select level of difficulty)
2. Tiles and symbols (game board)
3. Moves Counter
4. Accuracy Calculator
5. Game Over screen

### Classes
**```main.py```**
```
class Tile:
    def __init__(self, symbol, x, y, width, height):
        """
        Initialize a Tile object.

        Args:
            symbol (str): The symbol associated with the tile.
            x (int): The x-coordinate of the tile's position.
            y (int): The y-coordinate of the tile's position.
            width (int): The width of the tile.
            height (int): The height of the tile.
        """
        pass

    def draw(self, screen):
        """
        Draw the tile on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the tile on.
        """
        pass

    def reveal(self):
        """
        Reveals a tile.
        """
        pass

    def hide(self):
        """
        Hides a tile.
        pass

    def match_tile(self, other_tile):
        """
        Matches the tile with another tile.

        Args:
            other_tile (Tile): The other tile to match with.

        Returns:
            bool: True if the tiles match, False if they don't.
        """
        pass


class Game:
    def __init__(self, level, screen, width, height):
        """
        Initializes a Game object.

        Args:
            level (int): The level of the game.
            screen (pygame.Surface): The surface to draw the game on.
            width (int): The width of the game screen.
            height (int): The height of the game screen.
        """
        pass

    def initialize_level(self):
        """
        Initializes the game level.
        """
        pass

    def create_tiles(self):
        """
        Createa the tiles and arranges the grid for the game.
        """
        pass

    def draw_game_screen(self):
        """
        Draws the game screen
        """
        pass

    def on_tile_click(self, tile):
        """
        Detects/handles a click event on a tile.

        Args:
            tile (Tile): The clicked tile.
        """
        pass

    def is_game_over(self):
        """
        Check if the game is over.

        Returns:
            True if all tiles are matched, False if they're not.
        """
        pass

    def get_accuracy(self):
        """
        Get the accuracy of the player's moves.

        Returns:
            float: The accuracy as a percentage.
        """
        pass

    def get_moves(self):
        """
        Get the number of moves made by the player.

        Returns:
            int: The number of moves.
        """
        pass

    def handle_tile_click(self, pos):
        """
        Detects/handles a click event on the game screen.

        Args:
            pos: The position of the click event.
        """
        pass
```

**```controller.py```**
```
class Controller:
    def __init__(self, screen, width, height):
        """
        Initializes a Controller class.
        
        Args:
            screen: The pygame screen to draw on.
            width: The width of the screen.
            height: The height of the screen.
        """
        pass

    def mainloop(self):
        """
        The main loop of the game. Handles events and updates the game state.
        """
        pass

    def handle_mouse_down(self, pos):
        """
        Handles the mouse down event for each state of the game.
        
        Args:
            pos: The position of the mouse click.
        """
        pass

    def handle_menu_click(self, pos):
        """
        Handles the menu click event.

        Args:
            pos: The position of the mouse click.
        """
        pass

    def handle_game_over_click(self, pos):
        """
        Handles the game over click event (redirects the user to beginning of game loop).

        Args:
            pos: The position of the mouse click.
        """

    def update_screen(self):
        """
        Updates the screen according the current state of the game.
        
        """

    def draw_checkerboard(self, color1, color2):
        """
        Draw a checkerboard pattern on the screen.
        """

    def draw_menu(self):
        """
        Draws the menu screen.
        """
        pass


    def draw_game_over_screen(self):
        """
        Draws the game over screen.
        """
        pass

    def get_level_from_pos(self, pos):
        """
        Determines the level number based on the position of the mouse.

        Args:
        - pos: A tuple representing the x and y coordinates of the position of the mouse.

        Returns:
        - The level number (1, 2, or 3) if the click is within one of the level rects.
        - None if the position is not within any of the level rects.
        """
 ```

## ATP
- You can access the ATP [here](atp.md).


