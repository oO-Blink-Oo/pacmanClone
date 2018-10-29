import pygame
from pygame.sprite import Sprite


class Pacman(Sprite):

    def __init__(self, screen, maze_things, position):
        """Initialized values"""
        super(Pacman, self).__init__()
        pygame.font.init()
        self.screen = screen
        # get the rect of the screen
        self.screen_rect = screen.get_rect()

        # get the rect of a brick to check for collision
        self.bricks = maze_things.bricks
        self.pellets = maze_things.pellets
        self.power_pellets = maze_things.powerPellets
        self.portal_one = maze_things.portal_one
        self.portal_two = maze_things.portal_two

        self.maze_properties = maze_things

        # Load the images for pacman
        self.pacRight = [pygame.image.load('images/r1.png'), pygame.image.load('images/r2.png')]
        self.pacLeft = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png')]
        self.pacUp = [pygame.image.load('images/U1.png'), pygame.image.load('images/U2.png')]
        self.pacDown = [pygame.image.load('images/D1.png'), pygame.image.load('images/D2.png')]
        self.pacman_idle = pygame.image.load('images/standby.png')

        self.image = self.pacRight[1]

        # Score
        self.score = 0

        # Pacman sounds
        self.eating_sound = pygame.mixer.Sound("sounds/waka1.wav")
        self.portal_sound = pygame.mixer.Sound("sounds/portal.wav")

        # Pacman speed
        self.speed = 5

        # Get rect of the image
        self.rect = self.pacman_idle.get_rect()

        # Lives
        self.livesImage = pygame.image.load('images/r1.png')
        self.livesLeftImages = []
        self.fruitEaten = []
        self.life_left = 3
        for x in range(self.life_left):
            self.livesLeftImages.append(self.livesImage)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # keeps track of what image to display
        self.walkCount = 0

        # Initial placement of pacman (w/o extending text file)
        self.rect.x = position[0] * self.maze_properties.brick.rect.width - 15
        self.rect.y = position[1] * self.maze_properties.brick.rect.height - 9

        # Extended text file initial position
        # self.rect.x = 307
        # self.rect.y = 524

        # center of the sprite
        self.center_horizontal = float(self.rect.centerx)
        self.center_vertical = float(self.rect.centery)

    def points_gathered(self):
        font = pygame.font.SysFont(None, 50)
        text = font.render("Score: " + str(self.score), True, (255, 255, 255))
        self.screen.blit(text, (10, 670))

    def update(self):
        for brick in self.bricks:
            if brick.colliderect(self.rect):

                if self.moving_right:
                    self.center_horizontal -= self.speed + 2
                    self.moving_right = False
                elif self.moving_left:
                    self.center_horizontal += self.speed + 2
                    self.moving_left = False
                elif self.moving_up:
                    self.center_vertical += self.speed + 2
                    self.moving_up = False
                elif self.moving_down:
                    self.center_vertical -= self.speed + 2
                    self.moving_down = False
                print("collide")

        for pellet in self.pellets:
            if pellet.colliderect(self.rect):
                pygame.mixer.Sound.play(self.eating_sound)
                self.score += 10
                self.pellets.remove(pellet)

        for power_pellet in self.power_pellets:
            if power_pellet.colliderect(self.rect):
                pygame.mixer.Sound.play(self.eating_sound)
                self.score += 300
                self.power_pellets.remove(power_pellet)

        for portal_one in self.portal_one:
            if portal_one.colliderect(self.rect):
                pygame.mixer.Sound.play(self.portal_sound)
                self.center_vertical = 435
                self.center_horizontal = 32

        for portal_two in self.portal_two:
            if portal_two.colliderect(self.rect):
                pygame.mixer.Sound.play(self.portal_sound)
                self.center_vertical = 32
                self.center_horizontal = 570

        if self.moving_right and self.rect.right < self.screen_rect.right:  # deals with edge of screen collisions
            self.center_horizontal += self.speed
            print("Horizonatal_position: " + str(self.center_horizontal) + " Vertical_position: "
                  + str(self.center_vertical))
        if self.moving_left and self.rect.left > - 25:
            self.center_horizontal -= self.speed
            print("Horizonatal_position: " + str(self.center_horizontal) + " Vertical_position: "
                  + str(self.center_vertical))
        if self.moving_up and self.rect.top > 0:
            self.center_vertical -= self.speed
            print("Horizonatal_position: " + str(self.center_horizontal) + " Vertical_position: "
                  + str(self.center_vertical))
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_vertical += self.speed
            print("Horizonatal_position: " + str(self.center_horizontal) + " Vertical_position: "
                  + str(self.center_vertical))

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
        # elif self.moving_left or self.center_horizontal < -30:
        #     self.center_vertical = 35
        #     self.center_horizontal = 570
        #     self.screen.blit(self.pacLeft[self.walkCount % 2], self.rect)
        #     self.walkCount += 1
        elif self.moving_up:
            self.screen.blit(self.pacUp[self.walkCount % 2], self.rect)
            self.walkCount += 1
        elif self.moving_down:
            self.screen.blit(self.pacDown[self.walkCount % 2], self.rect)
            self.walkCount += 1
        else:
            self.screen.blit(self.pacman_idle, self.rect)

        placement = 0
        for x in self.livesLeftImages:
            self.livesImageRect = x.get_rect()

            self.livesImageRect.center = self.screen_rect.center
            self.livesImageRect.y = 670
            self.livesImageRect.right = self.screen_rect.right - 330 + placement

            placement += 30

            self.screen.blit(x, self.livesImageRect)
