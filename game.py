# Ian Michael Jesu Alvarez
# Pacman clone
import pygame
from eventloop import EventLoop
from maze import Maze
from expandfile import ExpandFile
from pacman import Pacman
from ghost import Ghost


GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Game:

    def __init__(self):
        pygame.init()
        self.screen_width = 599
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Pacman')
        self.clock = pygame.time.Clock()


        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.hovered = False

        # self.blinky = Ghost(self.screen, self.maze, 'blinky')
        #self.ghosts = Group()

        # Give files needed to populate the maze
        self.expandfile = ExpandFile('test.txt', expandBy=2)
        self.maze = Maze(self.screen, 'test.txt', 'images/wall', 'images/foodPellet',
                         'images/portal_1', 'images/portal_2')

        self.player = Pacman(self.screen, self.maze, self.maze.pacmanposition)
        self.blinky = Ghost(self.screen, 'blinky', self.maze, self.maze.blinky_position, self.player)
        self.clyde = Ghost(self.screen, 'clyde', self.maze, self.maze.clyde_position, self.player)
        self.inkey = Ghost(self.screen, 'inkey', self.maze, self.maze.inkey_position, self.player)
        self.pinky = Ghost(self.screen, 'pinky', self.maze, self.maze.pinky_position, self.player)

        self.intro_music = pygame.mixer.Sound("sounds/intro.wav")

        self.intro_logo = pygame.image.load('images/pacmanLogo.png')

    def get_color(self):
        if not self.hovered:
            return (255, 255, 255)
        else:
            return (100, 100, 100)

    def game_intro(self):
        pygame.draw.rect(self.screen, (75, 80, 33), (0, 0, self.screen_width, self.screen_height))
        font = pygame.font.SysFont(None, 50)
        self.screen_text = font.render("Play", True, self.get_color())
        self.text_rect = self.screen_text.get_rect()

        self.screen.blit(self.screen_text, (270, 400))
        self.screen.blit(self.intro_logo, (110, 100))
        intro = True

        while intro:

            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(self.intro_music)
                    self.play()

            pygame.display.update()

    def play(self):
        eventloop = EventLoop(finished=False)

        while not eventloop.finished:
            self.clock.tick(30)
            eventloop.check_events(self.player)
            self.player.update()
            self.update_screen()

    def update_screen(self):
        self.screen.fill(self.BLACK)
        self.maze.blitme()
        self.player.blitme()
        self.blinky.blitme()
        self.clyde.blitme()
        self.inkey.blitme()
        self.pinky.blitme()
        # Draw scoreboard
        self.player.points_gathered()

        pygame.display.flip()


game = Game()
game.game_intro()
