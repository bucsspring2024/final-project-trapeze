import pygame
import random
import requests
import re
from controller import Controller

class Tile:
    def __init__(self, color, x, y, width, height):
        """
        Initialize a Tile object.

        Args:
            symbol (str): The symbol associated with the tile.
            x (int): The x-coordinate of the tile's position.
            y (int): The y-coordinate of the tile's position.
            width (int): The width of the tile.
            height (int): The height of the tile.
        """
        self.color = color
        self.is_hidden = True
        self.is_matched = False
        self.rect = pygame.Rect(x, y, width, height)
        
    def draw(self, screen):
        """
        Draw the tile on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the tile on.
        """
        pygame.draw.rect(screen, "black", (self.rect.x - 2, self.rect.y - 2, self.rect.width + 4, self.rect.height + 4))
        if self.is_hidden:
            pygame.draw.rect(screen, "white", self.rect)
        else: 
            if self.is_matched:
                color = "black" 
            else: 
                color = "white"
            pygame.draw.rect(screen, color, self.rect)
            pygame.draw.rect(screen, self.color, (self.rect.x + 5, self.rect.y + 5, self.rect.width - 10, self.rect.height - 10)) 
            
    def reveal(self):
        """
        Reveals the tile.
        """
        self.is_hidden = False
        
    def hide(self):
        """
        Hides the tile.
        """
        self.is_hidden = True
        
    def match_tile(self, other_tile):
        """
        Match the tile with another tile.

        Args:
            other_tile (Tile): The other tile to match with.

        Returns:
            True if the tiles match, False if they don't.
        """
        self.is_matched = True
        other_tile.is_matched = True
        return self.color == other_tile.color
    
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
        self.level = level
        self.screen = screen
        self.width = width
        self.height = height
        self.moves_counter = 0
        self.tiles = []
        self.selected_tile = None
        self.revealed_tiles = []
        self.controller = Controller(screen, width, height)
        self.initialize_level()
     
    def initialize_level(self):    
        """
        Initializes the game level.
        """
        if self.level == 1:
            self.rows, self.cols = 2, 4
            self.screen.fill((249, 219, 189))
        elif self.level == 2:
            self.rows, self.cols = 4, 4
            self.screen.fill((252, 161, 125))
        elif self.level == 3:
            self.rows, self.cols = 4, 6
            self.screen.fill((218, 98, 125))
        self.create_tiles()
        
    def create_tiles(self):
        """
        Create the tiles and arranges the grid for the game.
        """
        response = requests.get('https://x-colors.yurace.pro/api/random?number=12')
        color_dicts = response.json()
        colors = []
        for color_dict in color_dicts:
            rgb_str = color_dict['rgb']
            match = re.search(r'rgb\((\d+), (\d+), (\d+)\)', rgb_str)
            if match:
                r, g, b = map(int, match.groups())
                colors.append((r, g, b))
        
        if self.level == 1:
            num_colors = 4
        elif self.level == 2:
            num_colors = 8
        elif self.level == 3:
            num_colors = 12
            
        colors = colors[:num_colors] * 2
        random.shuffle(colors)
        
        gap_size = 10
        
        tile_width = (self.width - (self.cols + 1) * gap_size) / (self.cols * 2)
        tile_height = (self.height - (self.rows + 1) * gap_size) / (self.rows * 2)

        total_width = self.cols * tile_width + (self.cols + 1) * gap_size
        total_height = self.rows * tile_height + (self.rows + 1) * gap_size
        start_x = (self.width - total_width) // 2
        start_y = (self.height - total_height) // 2

        for row in range(self.rows):
            for col in range(self.cols):
                color = colors.pop()
                x = start_x + col * (tile_width + gap_size) + gap_size
                y = start_y + row * (tile_height + gap_size) + gap_size
                tile = Tile(color, x, y, tile_width, tile_height)
                self.tiles.append(tile)

                
    def draw_game_screen(self):
        """
        Draws the game screen.
        """
        colors = [(249, 219, 189), (252, 161, 125), (218, 98, 125)]
        if self.level == 1:
            self.controller.draw_checkerboard((243, 194, 145), (239, 173, 108))
        elif self.level == 2:
            self.controller.draw_checkerboard((251, 140, 96), (250, 111, 56))
        elif self.level == 3:
            self.controller.draw_checkerboard((198, 47, 79), (165, 39, 66))
        pygame.draw.rect(self.screen, colors[self.level - 1], (150, 150, self.width - 300, self.height - 300), 0)
        title = f"Level {self.level}"
        
        for tile in self.tiles:
            tile.draw(self.screen)
        title_font = pygame.font.SysFont("sfcompactrounded", 48)
        title_text = title_font.render(title, True, "black")
        title_text_x = (self.width - title_text.get_width()) // 2
        title_text_y = self.height // 5
        self.screen.blit(title_text, (title_text_x, title_text_y - 20))
        
        moves_font = pygame.font.SysFont("sfcompactrounded", 36)
        moves_text = moves_font.render(f"Moves: {self.moves_counter}", True, "black")
        moves_x = 20 
        moves_y = 20
        self.screen.blit(moves_text, (moves_x, moves_y))
        
    
    def on_tile_click(self, tile):
        """
        Detects/handles a click event on a tile.

        Args:
            tile (Tile): The clicked tile.
        """
        if len(self.revealed_tiles) < 2 and not tile.is_matched:
            tile.reveal()
            self.revealed_tiles.append(tile)
            
        if len(self.revealed_tiles) == 2:
            tile1, tile2 = self.revealed_tiles
            if tile1.color == tile2.color:
                tile1.match_tile(tile2)
            else:
                pygame.time.wait(1000)
                tile1.hide()
                tile2.hide()
            self.revealed_tiles = []
                        
    def is_game_over(self):
        """
        Check if the game is over.

        Returns:
            True if all tiles are matched, False otherwise.
        """
        return all(tile.is_matched for tile in self.tiles)
    
    def get_accuracy(self):
        """
        Get the accuracy of the player.

        Returns:
            float: The accuracy as a percentage.
        """
        self.accuracy = (self.rows * self.cols) / self.moves_counter * 100
        return self.accuracy
    
    def get_moves(self):
        """
        Get the number of moves made by the player.

        Returns:
            int: The number of moves.
        """
        return self.moves_counter
    
    def handle_tile_click(self, pos):
        """
        Detects/handles a click event on the game screen.

        Args:
            pos: The position of the click event.
        """
        clicked_tile = None
        for tile in self.tiles:
            if tile.rect.collidepoint(pos) and tile.is_hidden:
                clicked_tile = tile
                break

        if clicked_tile:
            clicked_tile.reveal()
            self.moves_counter += 1
            if not self.selected_tile:
                self.selected_tile = clicked_tile
            else:
                if self.selected_tile.color == clicked_tile.color:
                    self.selected_tile.match_tile(clicked_tile)
                    self.selected_tile = None
                else:
                    self.selected_tile.hide()
                    self.selected_tile = clicked_tile

def main():
    pygame.init()
    width = 1440
    height = 900
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tile Matching Game")
    
    controller = Controller(screen, width, height)
    controller.mainloop()
    
    pygame.quit()
    
if __name__ == "__main__":
    main()
