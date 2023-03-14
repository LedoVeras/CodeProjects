import sys
import pip

import pygame
from pygame.locals import *


class AlienInvasion:
    """Overall class to manage the game."""
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
             (1200, 800))
        pygame.display.set_caption(
                "Alien Invasion")
        
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            self.clock.tick(60)
            
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()