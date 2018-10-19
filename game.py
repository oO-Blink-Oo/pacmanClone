# Ian Michael Jesu Alvarez

import pygame
from eventloop import EventLoop
from maze import Maze
from expandfile import ExpandFile
from pacman import Pacman
from scoreboard import Scoreboard
from time import sleep


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 800))
        pygame.display.set_caption('Pacman')
        self.clock = pygame.time.Clock()

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # Give files needed to populate the maze
        self.expandfile = ExpandFile('test.txt', expandBy=2)
        self.maze = Maze(self.screen, 'test.txt', 'images/wall', 'images/foodPellet')

        # Create a scoreboard
        self.sb = Scoreboard(self.screen, self.maze)

        self.intro_music = pygame.mixer.Sound("sounds/intro.wav")

        self.player = Pacman(self.screen, self.maze)

    # def __str__(self): return

    def play(self):
        eventloop = EventLoop(finished=False)
        pygame.mixer.Sound.play(self.intro_music)
        while not eventloop.finished:
            self.clock.tick(30)
            eventloop.check_events(self.screen, self.player)
            self.player.update()
            self.update_screen()

    def update_screen(self):
        self.screen.fill(self.BLACK)
        self.maze.blitme()
        self.player.blitme()

        # Draw scoreboard
        self.sb.show_score()
        pygame.display.flip()


game = Game()
game.play()
