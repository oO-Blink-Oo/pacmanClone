import pygame
from pygame.sprite import Sprite

from maze import Maze
from imagerect import ImageRect



class Pacman(Sprite):

    def __init__(self, screen, maze_things):
        """Initialized values"""
        super(Pacman, self).__init__()
        self.screen = screen
        # get the rect of the screen
        self.screen_rect = screen.get_rect()

        # get the rect of a brick to check for collision
        self.bricks = maze_things.bricks
        self.pellets = maze_things.pellets

        self.maze_properties = maze_things
        # Load the images for pacman
        self.pacRight = [pygame.image.load('images/r1.png'), pygame.image.load('images/r2.png')]
        self.pacLeft = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png')]
        self.pacUp = [pygame.image.load('images/U1.png'), pygame.image.load('images/U2.png')]
        self.pacDown = [pygame.image.load('images/D1.png'), pygame.image.load('images/D2.png')]
        self.pacman_idle = pygame.image.load('images/standby.png')

        self.image = self.pacRight[1]

        # Pacman sounds
        self.eating_sound = pygame.mixer.Sound("sounds/waka1.wav")

        # Pacman speed
        self.speed = 3

        # Get rect of the image
        self.rect = self.pacman_idle.get_rect()

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # keeps track of what image to display
        self.walkCount = 0

        # Initial placement of pacman (w/o extending text file)
        self.rect.x = 285
        self.rect.y = 485

        # Extended text file initial position
        # self.rect.x = 307
        # self.rect.y = 524

        # center of the sprite
        self.center_horizontal = float(self.rect.centerx)
        self.center_vertical = float(self.rect.centery)

    def update(self):
        for brick in self.bricks:
            if brick.colliderect(self.rect):

                if self.moving_right:
                    self.center_horizontal -= self.speed
                    self.moving_right = False
                elif self.moving_left:
                    self.center_horizontal += self.speed
                    self.moving_left = False
                elif self.moving_up:
                    self.center_vertical += self.speed
                    self.moving_up = False
                elif self.moving_down:
                    self.center_vertical -= self.speed
                    self.moving_down = False
                print("collide")

        for pellet in self.pellets:
            if pellet.colliderect(self.rect):
                pygame.mixer.Sound.play(self.eating_sound)
                self.pellets.remove(pellet)

        if self.moving_right and self.rect.right < self.screen_rect.right:  # deals with edge of screen collisions
            self.center_horizontal += self.speed
        if self.moving_left and self.rect.left > 0:
            self.center_horizontal -= self.speed
        if self.moving_up and self.rect.top > 0:
            self.center_vertical -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_vertical += self.speed

        # Update rect object from self.center.
        self.rect.centerx = self.center_horizontal
        self.rect.centery = self.center_vertical

    def blitme(self):
        """Draw pacman at its current location."""
        if self.walkCount + 1 >= 10:
            self.walkCount = 0

        if self.moving_right:
            self.screen.blit(self.pacRight[self.walkCount % 2], self.rect)
            self.walkCount += 1
        elif self.moving_left:
            self.screen.blit(self.pacLeft[self.walkCount % 2], self.rect)
            self.walkCount += 1
        elif self.moving_up:
            self.screen.blit(self.pacUp[self.walkCount % 2], self.rect)
            self.walkCount += 1
        elif self.moving_down:
            self.screen.blit(self.pacDown[self.walkCount % 2], self.rect)
            self.walkCount += 1
        else:
            self.screen.blit(self.pacman_idle, self.rect)



    # make a reset position for pacman for new game or death

# Ask Professor
# how to get the rect of a list of loaded images
