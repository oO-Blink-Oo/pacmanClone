import pygame
import sys


def check_keydown_events(event, player):
    """Respond to key presses"""
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right.
        player.moving_right = True
        player.moving_left = False
        player.moving_up = False
        player.moving_down = False
    elif event.key == pygame.K_LEFT:
        # Move the ship to the left.
        player.moving_left = True
        player.moving_right = False
        player.moving_up = False
        player.moving_down = False
    elif event.key == pygame.K_UP:
        # Move the ship to the left.
        player.moving_left = False
        player.moving_right = False
        player.moving_up = True
        player.moving_down = False
    elif event.key == pygame.K_DOWN:
        # Move the ship to the left.
        player.moving_left = False
        player.moving_right = False
        player.moving_up = False
        player.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, player):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
    elif event.key == pygame.K_LEFT:
        player.moving_left = False
    elif event.key == pygame.K_UP:
        player.moving_up = False
    elif event.key == pygame.K_DOWN:
        player.moving_down = False


class EventLoop:
    def __init__(self, finished):
        self.finished = finished

    def __str__(self):
        return 'eventloop, finished=' + str(self.finished) + ')'

    @staticmethod
    def check_events(screen, player):

        screen_rect = screen.get_rect()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, player)

            # Leave this commented to make player keep moving in one key press
            # elif event.type == pygame.KEYUP:
            #     check_keyup_events(event, player)

