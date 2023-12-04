'''
Author: luhaifeng666 youzui@hotmail.com
Date: 2023-11-09 16:29:32
LastEditors: haifeng.lu
LastEditTime: 2023-12-04 23:52:19
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

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._unpdate_screen()

    def _check_events(self):
      # 响应按键和鼠标事件
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        elif event.type == pygame.KEYDOWN:
          self.check_key_down(event)
        elif event.type == pygame.KEYUP:
          self.check_key_up(event)
            
    def check_key_down(self, event):
      if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        self.ship.moving_right = True
      elif event.key == pygame.K_LEFT:
        self.ship.moving_left = True
      elif event.key == pygame.K_q:
        sys.exit()
    
    def check_key_up(self, event):
      if event.key == pygame.K_RIGHT:
        self.ship.moving_right = False
      elif event.key == pygame.K_LEFT:
        self.ship.moving_left = False
          
    def _unpdate_screen(self):
      # 更新屏幕上的颜色，并切换到新屏幕
      self.screen.fill(self.settings.bg_color)
      self.ship.blitme()
      
      pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
