'''
Author: luhaifeng666 youzui@hotmail.com
Date: 2023-11-13 14:06:59
LastEditors: haifeng.lu
LastEditTime: 2023-12-04 23:42:38
FilePath: /alien-invasion/ship.py
Description: 

'''
import pygame


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞创图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom
        
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        
        # 飞船设置
        self.ship_speed = 1.5
        
        # 在飞船的属性x中存储小数值
        self.x = float(self.rect.x)
        
    def update(self):
      # 飞船的右边缘坐标小于屏幕的右侧边缘坐标时，可以向右移动
      if self.moving_right and self.rect.right < self.screen_rect.right:
        self.x += self.ship_speed
      # 飞船的左侧边缘坐标 > 0 时，可以向左移动
      if self.moving_left and self.rect.left > 0:
        self.x -= self.ship_speed
        
      self.rect.x = self.x  

    def blitme(self):
        # 在指定位置绘制飞船

        self.screen.blit(self.image, self.rect)
