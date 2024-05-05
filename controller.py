import pygame

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
 
class Controller:
    def __init__(self):
        """
        Initialize the controller with pygame data.
        args: None
        """
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("My Game")
    def mainloop(self):
        """
        Loop of some sort.
        args: None
        """
        while(True): #this can also be a variable instead of just True
            #1. Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            #2. detect collisions and update models

            #3. Redraw next frame

            #4. Display next frame
            pygame.display.flip()
        