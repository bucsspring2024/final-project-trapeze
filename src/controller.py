import pygame
import time

class Controller:
    def __init__(self, screen, width, height):
        """
        Initializes the Controller class.
        
        Args:
            screen: The pygame screen to draw on.
            width: The width of the screen.
            height: The height of the screen.
        """
        self.screen = screen
        self.width = width
        self.height = height
        self.state = "welcome"
        self.level = None
        self.game = None
        
        self.font_large = pygame.font.Font(None, 56)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_xlarge = pygame.font.Font(None, 100)

    def mainloop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_down(event.pos)
                    
            self.update_screen()
            pygame.display.flip()
        pygame.quit()
        
    def handle_mouse_down(self, pos):
        """
        Handles/detects the mouse down event for each state of the game.
        
        Args:
            pos: The position of the mouse click.
        """
        if self.state == "welcome":
            self.handle_menu_click(pos)
        elif self.state == "game":
            self.game.handle_tile_click(pos)
        elif self.state == "game_over":
            self.handle_game_over_click(pos)

    def handle_menu_click(self, pos):
        """
        Handles/detects the menu click event.

        Args:
            pos: The position of the mouse click.
        """
        level = self.get_level_from_pos(pos)
        if level is not None:
            from main import Game
            self.game = Game(level, self.screen, self.width, self.height)
            self.level = level
            self.state = "game"

    def handle_game_over_click(self, pos):
        """
        Handles/detects the game over click event (redirects the user to beginning of game loop).

        Args:
            pos: The position of the mouse click.
        """
        self.state = "welcome"

    def update_screen(self):
        """
        Updates the screen according the current state of the game.
        
        """
        if self.state == "welcome":
            self.draw_menu()
        elif self.state == "game":
            if self.game.is_game_over():
                self.state = "game_over"
            self.game.draw_game_screen()
        elif self.state == "game_over":
            self.draw_game_over_screen()

    def draw_checkerboard(self, color1, color2):
        """
        Draws the checkerboard pattern background on the screen.
        """
        square_size = min(self.width, self.height) // 8
        rows = self.height // square_size
        cols = self.width // square_size
        
        for row in range(rows + 1):
            for col in range(cols + 1):
                if (row + col) % 2 == 0:
                    color = color1
                else:
                    color = color2
                pygame.draw.rect(self.screen, color, (col * square_size, row * square_size, square_size, square_size))
                
    def draw_menu(self):
        """
        Draws the main menu screen.
        """
        self.screen.fill((189, 219, 249))
        self.draw_checkerboard((138, 191, 244), (93, 167, 240))
        pygame.draw.rect(self.screen, (18, 108, 198), (140, 140, self.width - 280, self.height - 280), 0)
        pygame.draw.rect(self.screen, "white", (150, 150, self.width - 300, self.height - 300), 0)
    
        
        heading_font = pygame.font.SysFont("signpainter", 100)
        heading_text = heading_font.render("Match Mania!", True, (18, 108, 198))
        heading_text_x = (self.width - heading_text.get_width()) // 2
        heading_text_y = self.height // 4 - 100
        
        heading_text_shadow = heading_font.render("Match Mania!", True, (138, 191, 244))
        self.screen.blit(heading_text_shadow, (heading_text_x + 3, heading_text_y + 57))
        self.screen.blit(heading_text, (heading_text_x, heading_text_y + 54))
        
        title_font = pygame.font.SysFont("sfcompactrounded", 36)
        title_text = title_font.render("Choose a Level:", True, "white")
        title_text_x = (self.width - title_text.get_width()) // 2
        title_text_y = self.height // 3 + 10
        title_rect = pygame.Rect(title_text_x - 10, title_text_y - 10, title_text.get_width() + 20, title_text.get_height() + 20)
        pygame.draw.rect(self.screen, (18, 108, 198), title_rect, 0)
        self.screen.blit(title_text, (title_text_x, title_text_y))
        
        levels = [
            (self.width / 5, self.height / 4 + 200, self.width / 6, 240),
            (self.width / 2 - self.width / 12, self.height / 4 + 200, self.width / 6, 240),
            (4 * self.width / 5 - self.width / 6, self.height / 4 + 200, self.width / 6, 240)
        ]
        level_texts = ["1", "2", "3"]
        level_descriptions = ["8 tiles", "16 tiles", "24 tiles"]
        level_colors = [(249, 219, 189), (252, 161, 125), (218, 98, 125)]
        text_colors = [(238, 153, 68), (249, 82, 16), (165, 39, 66)]

        for i in range(3):
            shadow_offset = 10
            shadow_rect = pygame.Rect(levels[i][0] + shadow_offset, levels[i][1] + shadow_offset, levels[i][2], levels[i][3])
            pygame.draw.rect(self.screen, (138, 191, 244), shadow_rect, 0)
            
            pygame.draw.rect(self.screen, level_colors[i], levels[i], 0)
            level_text_font = pygame.font.SysFont("sfcompactrounded", 100)
            level_text = level_text_font.render(level_texts[i], True, text_colors[i])
            level_text_x = levels[i][0] + (levels[i][2] - level_text.get_width()) // 2
            level_text_y = levels[i][1] + (levels[i][3] - level_text.get_height()) // 2
            self.screen.blit(level_text, (level_text_x, level_text_y))
            
            level_desc_font = pygame.font.SysFont("sfcompactrounded", 36)
            level_desc = level_desc_font.render(level_descriptions[i], True, "black")
            level_desc_x = levels[i][0] + (levels[i][2] - level_desc.get_width()) // 2
            level_desc_y = levels[i][1] + (levels[i][3] - level_desc.get_height()) // 2 + 100
            self.screen.blit(level_desc, (level_desc_x, level_desc_y - 35)) 
            
    def draw_game_over_screen(self):
        """
        Draws the game over screen.
        """
        self.draw_checkerboard((138, 191, 244), (93, 167, 240))
        pygame.draw.rect(self.screen, (18, 108, 198), (0, 0, self.width, self.height), 150)
        pygame.draw.rect(self.screen, (201, 226, 250), (0, 0, self.width, self.height), 130)
        
        game_over_font = pygame.font.SysFont("signpainter", 100)
        game_over_text = game_over_font.render("Game Over!", True, "white")
        game_over_x = (self.width - game_over_text.get_width()) // 2
        game_over_y = (self.height - game_over_text.get_height()) // 3
        pygame.Rect(game_over_x - 10, game_over_y - 10, game_over_text.get_width() + 20, game_over_text.get_height() - 50)
        
        game_over_text_shadow = game_over_font.render("Game Over!", True, (18, 108, 198))
        self.screen.blit(game_over_text_shadow, (game_over_x + 5, game_over_y + 5))
        self.screen.blit(game_over_text, (game_over_x, game_over_y))
        
        accuracy = self.game.get_accuracy()
        accuracy_font = pygame.font.SysFont("sfcompactrounded", 36)
        accuracy_text = accuracy_font.render(f"Accuracy: {accuracy:.2f}%", True, "white")
        accuracy_x = (self.width - accuracy_text.get_width()) / 2
        accuracy_y = self.height / 2
        accuracy_rect = pygame.Rect(accuracy_x - 10, accuracy_y - 10, accuracy_text.get_width() + 20, accuracy_text.get_height() + 20)
        pygame.draw.rect(self.screen, (18, 108, 198), accuracy_rect, 0)
        self.screen.blit(accuracy_text, (accuracy_x, accuracy_y))
        
        moves = self.game.get_moves()
        moves_font = pygame.font.SysFont("sfcompactrounded", 36)
        moves_text = moves_font.render(f"You won in {moves} moves!", True, "white")
        moves_x = (self.width - moves_text.get_width()) / 2
        moves_y = accuracy_y + 50
        moves_rect = pygame.Rect(moves_x - 10, moves_y - 10, moves_text.get_width() + 20, moves_text.get_height() + 20)
        pygame.draw.rect(self.screen, (18, 108, 198), moves_rect, 0)
        self.screen.blit(moves_text, (moves_x, moves_y))
        
        back_to_menu_font = pygame.font.SysFont("sfcompactrounded", 36)
        back_to_menu_text = back_to_menu_font.render("Back to Menu", True, (18, 108, 198))
        back_to_menu_x = (self.width - back_to_menu_text.get_width()) // 2
        back_to_menu_y = moves_y + 100
        back_to_menu_rect = pygame.Rect(back_to_menu_x - 10, back_to_menu_y - 10, back_to_menu_text.get_width() + 20, back_to_menu_text.get_height() + 20)
        pygame.draw.rect(self.screen, "white", back_to_menu_rect, 0)
        self.screen.blit(back_to_menu_text, (back_to_menu_x, back_to_menu_y))

    def get_level_from_pos(self, pos):
        """
        Determines the level number based on the position of the mouse.

        Args:
        - pos: A tuple representing the x and y coordinates of the position of the mouse.

        Returns:
        - The level number (1, 2, or 3) if the click is within one of the level rects.
        - None if the position is not within any of the level rects.
        """
        levels = [
            pygame.Rect(self.width / 5, self.height / 4 + 200, self.width / 6, 240),
            pygame.Rect(self.width / 2 - 30, self.height / 4 + 200, self.width / 6, 240),
            pygame.Rect(4 * self.width / 5 - self.width / 6, self.height / 4 + 200, self.width / 6, 240)
        ]
        for i, rect in enumerate(levels, 1):
            if rect.collidepoint(pos):
                return i
        return None
