# Ian Michael Jesu Alvarez

import pygame
from eventloop import EventLoop
from maze import Maze
from expandfile import ExpandFile
from pacman import Pacman

class Game:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 665))
        pygame.display.set_caption('Pacman')

        # Create a pacman object to pass to maze

        # Give files needed to populate the maze
        self.expandfile = ExpandFile('test.txt', expandBy=2)
        self.maze = Maze(self.screen, 'test.txt', 'images/wall', 'images/foodPellet')

        self.player = Pacman(self.screen)

    # def __str__(self): return

    def play(self):
        eventloop = EventLoop(finished=False)

        while not eventloop.finished:
            eventloop.check_events(self.player)
            self.update_screen()

    def update_screen(self):
        self.screen.fill(Game.BLACK)
        self.maze.blitme()
        self.player.blitme()
        pygame.display.flip()


game = Game()
game.play()
