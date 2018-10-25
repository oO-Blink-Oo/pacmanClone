import pygame
from imagerect import ImageRect
from ghost import Ghost
# from pacman import Pacman


class Maze:
    RED = (255, 0, 0)
    BRICK_SIZE = 13  # 7 if extended
    # PACMAN_SIZE = 20
    # PELLET_SIZE = 4
    # POWER_PELLET_SIZE = 10

    def __init__(self, screen, mazefile, brickfile, pelletfile, portal_1, portal_2):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.bricks = []
        self.pellets = []
        self.powerPellets = []
        self.portal_one = []
        self.portal_two = []
        self.ghosts = []
        self.blinky_obj = Ghost(screen, 'blinky')
        # self.ghosts = ghosts

        sz = Maze.BRICK_SIZE
        # pelletsize = Maze.PELLET_SIZE
        # power_pellet_size = Maze.POWER_PELLET_SIZE
        self.brick = ImageRect(screen, brickfile, sz, sz)
        self.pellet = ImageRect(screen, pelletfile, int(.5*sz), int(.5*sz))
        self.powerPellet = ImageRect(screen, pelletfile, int(1*sz), int(1*sz))
        self.portal_1 = ImageRect(screen, portal_1, sz, 50)  # screen, image, width, height
        self.portal_2 = ImageRect(screen, portal_2, sz, 50)

        self.deltax = self.deltay = Maze.BRICK_SIZE

        self.build()

    def __str__(self): return 'maze(' + self.filename + ')'

    def build(self):
        r = self.brick.rect
        pellet = self.pellet.rect
        portal = self.portal_1.rect
        w, h = r.width, r.height
        p_w, p_h = pellet.width, pellet.height
        port_w, port_h = portal.width, portal.height
        dx, dy = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'X':
                    self.bricks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                if col == 'f':
                    self.pellets.append(pygame.Rect(ncol * dx, nrow * dy, p_w, p_h))
                if col == 'F':
                    self.powerPellets.append(pygame.Rect(ncol * dx, nrow * dy, p_w, p_h))
                if col == 'P':
                    self.portal_one.append(pygame.Rect(ncol * dx, nrow * dy, port_w, port_h))
                if col == 'p':
                    self.portal_two.append(pygame.Rect(ncol * dx, nrow * dy, port_w, port_h))
                if col == '1':
                    self.ghosts.append(self.blinky_obj)

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)

        for pelletrect in self.pellets:
            self.screen.blit(self.pellet.image, pelletrect)

        for portal_rect in self.portal_one:
            self.screen.blit(self.portal_1.image, portal_rect)

        for portal_rect in self.portal_two:
            self.screen.blit(self.portal_2.image, portal_rect)

        for powerrect in self.powerPellets:
            self.screen.blit(self.powerPellet.image, powerrect)

        for blinky in self.ghosts:
            self.screen.blit(self.blinky_obj.image, blinky)
