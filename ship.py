'''
Author: luhaifeng666 youzui@hotmail.com
Date: 2023-11-13 14:06:59
LastEditors: luhaifeng666 youzui@hotmail.com
LastEditTime: 2023-11-13 14:10:40
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

    def blitme(self):
        # 在指定位置绘制飞船

        self.screen.blit(self.image, self.rect)
