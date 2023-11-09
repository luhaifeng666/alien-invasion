'''
Author: luhaifeng666 youzui@hotmail.com
Date: 2023-11-09 16:29:32
LastEditors: luhaifeng666 youzui@hotmail.com
LastEditTime: 2023-11-09 16:34:42
FilePath: /alien-invasion/alien_invasion.py
Description: 

'''
import sys
import pygame


class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
