import pygame
from imagerect import ImageRect
# from pacman import Pacman


class Maze:
    RED = (255, 0, 0)
    BRICK_SIZE = 13
    # PACMAN_SIZE = 20
    # PELLET_SIZE = 4
    # POWER_PELLET_SIZE = 10

    def __init__(self, screen, mazefile, brickfile, pelletfile):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.bricks = []
        self.pellets = []
        self.powerPellets = []

        sz = Maze.BRICK_SIZE
        # pelletsize = Maze.PELLET_SIZE
        # power_pellet_size = Maze.POWER_PELLET_SIZE
        self.brick = ImageRect(screen, brickfile, sz, sz)
        self.pellet = ImageRect(screen, pelletfile, int(.5*sz), int(.5*sz))
        # self.powerPellet = ImageRect(screen, pelletfile, power_pellet_size, power_pellet_size)

        self.deltax = self.deltay = Maze.BRICK_SIZE

        self.build()

    def __str__(self): return 'maze(' + self.filename + ')'

    def build(self):
        r = self.brick.rect
        pellet = self.pellet.rect
        w, h = r.width, r.height
        dx, dy = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'X':
                    self.bricks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                if col == 'f':
                    self.pellets.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                if col == 'F':
                    self.powerPellets.append(pygame.Rect(ncol * dx, nrow * dy, pellet.width, pellet.height))

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)

        for pelletrect in self.pellets:
            self.screen.blit(self.pellet.image, pelletrect)

        # for powerrect in self.powerPellets:
        #     self.screen.blit(self.powerPellet.image, powerrect)
