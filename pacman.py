import pygame
from pygame.sprite import Sprite


class Pacman(Sprite):

    def __init__(self, screen):
        """Initialized values"""
        super(Pacman, self).__init__()
        self.screen = screen
        # get the rect of the screen
        self.screen_rect = screen.get_rect()

        # Load the images for pacman
        # self.pacRight = [pygame.image.load('Pacman/r1.png'), pygame.image.load('Pacman/r2.png')]
        # self.pacLeft = [pygame.image.load('Pacman/L1.png'), pygame.image.load('Pacman/L2.png')]
        # self.pacUp = [pygame.image.load('Pacman/U1.png'), pygame.image.load('Pacman/U2.png')]
        # self.pacDown = [pygame.image.load('Pacman/D1.png'), pygame.image.load('Pacman/D2.png')]
        self.pacman_idle = pygame.image.load('images/standby.png')

        # Pacman speed
        self.speed = 5

        # Get rect of the image
        self.rect = self.pacman_idle.get_rect()

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.walkCount = 0

        # Initial placement of pacman
        self.rect.x = 285
        self.rect.y = 485

        # center of the sprite
        self.center_horizontal = float(self.rect.centerx)
        self.center_vertical = float(self.rect.centery)

        y = 400
        speed = 5

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_horizontal += self.speed
        if self.moving_left and self.rect.right < self.screen_rect.right:
            self.center_horizontal -= self.speed
        if self.moving_up and self.rect.right < self.screen_rect.right:
            self.center_vertical -= self.speed
        if self.moving_down and self.rect.right < self.screen_rect.right:
            self.center_vertical += self.speed

    def blitme(self):
        """Draw pacman at its current location."""
        self.screen.blit(self.pacman_idle, self.rect)

    # make a reset position for pacman for new game or death

# Ask Professor
# how to get the rect of a list of loaded images
