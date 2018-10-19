import pygame.font
from pygame.sprite import Group
from pacman import Pacman

class Scoreboard():
    """A class to report scoring information."""
    def __init__(self, screen, maze_things):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.maze_things = maze_things

        self.score = 0

        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.pac_left = 3

        # Prepare the initial score image.
        self.prep_score()
        self.prep_ships()

    def prep_ships(self):
        """Show how many pacmans are left."""
        self.pacmans = Group()
        for pac_number in range(self.pac_left):
            pacman = Pacman(self.screen, self.maze_things)
            pacman.rect.x = 10 + pac_number*pacman.rect.width
            pacman.rect.y = 670
            self.pacmans.add(pacman)

    def show_score(self):
        """Draw score and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)

        # Draw ships.
        self.pacmans.draw(self.screen)

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, (0, 0, 0))

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 335
        self.score_rect.top = 670
        # rounded_score = int(round(self.stats.score, -1))
        # score_str = "{:,}".format(rounded_score)
        # self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

    def reset_stats(self):
        """Initilaize statistics that can change during the game."""
        self.pac_left = 3
        self.score = 0