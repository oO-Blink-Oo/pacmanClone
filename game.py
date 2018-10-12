# Ian Michael Jesu Alvarez

import pygame
from eventloop import EventLoop
from maze import Maze


class Game:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption('Pacman')

        self.maze = Maze(self.screen, 'test.txt', 'brick')

    # def __str__(self): return

    def play(self):
        eventloop = EventLoop(finished=False)

        while not eventloop.finished:
            eventloop.check_events()
            self.update_screen()

    def update_screen(self):
        self.screen.fill(Game.BLACK)
        self.maze.blitme()
        pygame.display.flip()


game = Game()
game.play()
