'''
Author: luhaifeng666 youzui@hotmail.com
Date: 2023-11-09 16:29:32
LastEditors: luhaifeng666
LastEditTime: 2023-11-29 23:29:04
FilePath: /alien-invasion/alien_invasion.py
Description: 

'''
import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self._unpdate_screen()

    def _check_events(self):
      # 响应按键和鼠标事件
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
          
    def _unpdate_screen(self):
      # 更新屏幕上的颜色，并切换到新屏幕
      self.screen.fill(self.settings.bg_color)
      self.ship.blitme()
      
      pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
