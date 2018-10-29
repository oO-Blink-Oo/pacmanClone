import pygame
from pygame.sprite import Sprite


class Ghost(Sprite):

    def __init__(self, screen, ghost_type, maze_things, position, pacman):
        """Initialized values"""
        super(Ghost, self).__init__()
        pygame.font.init()
        self.screen = screen
        # get the rect of the screen
        self.screen_rect = screen.get_rect()

        # get the rect of a brick to check for collision
        # self.bricks = maze_things.bricks
        self.maze_properties = maze_things
        self.pacman = pacman

        self.ghost_name = ghost_type
        self.is_vulnerable = False
        self.power_pellets = maze_things.powerPellets

        for power_pellet in self.power_pellets:
            if power_pellet.colliderect(self.pacman.rect):
                # pygame.mixer.Sound.play(self.eating_sound)
                # self.score += 300
                # self.power_pellets.remove(power_pellet)
                self.is_vulnerable = True

        self.points = 100
        self.vulnerable_points = 300

        # Load the images for Blinky
        if ghost_type == 'blinky'and not self.is_vulnerable:
            self.blinky_right = [pygame.image.load('images/Blinky/R1.png'), pygame.image.load('images/Blinky/R2.png')]
            self.blinky_left = [pygame.image.load('images/Blinky/L1.png'), pygame.image.load('images/Blinky/L2.png')]
            self.blinky_up = [pygame.image.load('images/Blinky/U1.png'), pygame.image.load('images/Blinky/U2.png')]
            self.blinky_down = [pygame.image.load('images/Blinky/D1.png'), pygame.image.load('images/Blinky/D2.png')]
            self.image = self.blinky_right[0]
            self.idle = pygame.image.load('images/Blinky/R1.png')
            self.rect = self.image.get_rect()
        elif ghost_type == 'blinky' and self.is_vulnerable:
            """Turn ghost to vulnerable"""
            self.vulnerable_ghost = [pygame.image.load('images/Vulnerable/V1.png'),
                                     pygame.image.load('images/Vulnerable/V2.png')]
            self.image = self.vulnerable_ghost[0]
            self.idle = pygame.image.load('images/Vulnerable/V1.png')
            self.rect = self.image.get_rect()
        elif ghost_type == 'clyde' and not self.is_vulnerable:
            # Load the images for Clyde
            self.clyde_right = [pygame.image.load('images/Clyde/R1.png'), pygame.image.load('images/Clyde/R2.png')]
            self.clyde_left = [pygame.image.load('images/Clyde/L1.png'), pygame.image.load('images/Clyde/L2.png')]
            self.clyde_up = [pygame.image.load('images/Clyde/U1.png'), pygame.image.load('images/Clyde/U2.png')]
            self.clyde_down = [pygame.image.load('images/Clyde/D1.png'), pygame.image.load('images/Clyde/D2.png')]
            self.image = self.clyde_right[0]
            self.idle = pygame.image.load('images/Clyde/R1.png')
            self.rect = self.image.get_rect()
        elif ghost_type == 'inkey' and not self.is_vulnerable:
            # Load the images for Inkey
            self.inkey_right = [pygame.image.load('images/Inkey/R1.png'), pygame.image.load('images/Inkey/R2.png')]
            self.inkey_left = [pygame.image.load('images/Inkey/L1.png'), pygame.image.load('images/Inkey/L2.png')]
            self.inkey_up = [pygame.image.load('images/Inkey/U1.png'), pygame.image.load('images/Inkey/U2.png')]
            self.inkey_down = [pygame.image.load('images/Inkey/D1.png'), pygame.image.load('images/Inkey/D2.png')]
            self.image = self.inkey_right[0]
            self.idle = pygame.image.load('images/Inkey/R1.png')
            self.rect = self.image.get_rect()
        elif ghost_type == 'pinky' and not self.is_vulnerable:
            # Load the images for Pinky
            self.pinky_right = [pygame.image.load('images/Pinky/R1.png'), pygame.image.load('images/Pinky/R2.png')]
            self.pinky_left = [pygame.image.load('images/Pinky/L1.png'), pygame.image.load('images/Pinky/L2.png')]
            self.pinky_up = [pygame.image.load('images/Pinky/U1.png'), pygame.image.load('images/Pinky/U2.png')]
            self.pinky_down = [pygame.image.load('images/Pinky/D1.png'), pygame.image.load('images/Pinky/D2.png')]
            self.image = self.pinky_right[0]
            self.idle = pygame.image.load('images/Pinky/R1.png')
            self.rect = self.image.get_rect()

        self.vulnerable_ghost = [pygame.image.load('images/Vulnerable/V1.png'),
                                 pygame.image.load('images/Vulnerable/V2.png')]

        # self.image = self.blinky_up[1]  # this is for Blinky

        # ghost sounds
        # self.eating_sound = pygame.mixer.Sound("sounds/waka1.wav")

        # Ghost speed
        self.speed = 5

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # keeps track of what image to display
        self.walkCount = 0

        # Get rect of the chosen image

        # Initial placement of ghost (w/o extending text file)
        if ghost_type == 'blinky':
            self.rect.x = position[0] * self.maze_properties.brick.rect.width
            self.rect.y = position[1] * self.maze_properties.brick.rect.height
        elif ghost_type == 'clyde':
            self.rect.x = position[0] * self.maze_properties.brick.rect.width
            self.rect.y = position[1] * self.maze_properties.brick.rect.height
        elif ghost_type == 'inkey':
            self.rect.x = position[0] * self.maze_properties.brick.rect.width
            self.rect.y = position[1] * self.maze_properties.brick.rect.height
        elif ghost_type == 'pinky':
            self.rect.x = position[0] * self.maze_properties.brick.rect.width
            self.rect.y = position[1] * self.maze_properties.brick.rect.height
        else:
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
        # center of the sprite
        self.center_horizontal = float(self.rect.centerx)
        self.center_vertical = float(self.rect.centery)
        # self.x = float(self.rect.x)
        # self.y = float(self.rect.y)
        # self.center = float(self.rect.centerx)

        # Extended text file initial position
        # self.rect.x = 307
        # self.rect.y = 524
        self.blitme()

    def update(self):

        if self.moving_right:
            self.rect.centerx += self.speed
        elif self.moving_left:
            self.rect.centerx -= self.speed
        elif self.moving_up:
            self.rect.centery += self.speed
        elif self.moving_down:
            self.rect.centerx += self.speed

        # Update rect object from self.center.
        self.rect.centerx = self.center_horizontal
        self.rect.centery = self.center_vertical
        self.blitme()

    def blitme(self):
        if self.walkCount + 1 >= 10:
            self.walkCount = 0
        if not self.is_vulnerable:
            self.screen.blit(self.idle, self.rect)
        else:
            self.screen.blit(self.vulnerable_ghost[0], self.rect)
