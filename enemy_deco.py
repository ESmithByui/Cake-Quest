import pygame
import random

class Enemy_deco(pygame.sprite.Sprite):
    def __init__(self, enemy, type, var, color = 0):
        super().__init__()
        self.enemy = enemy

        if color == 0:
            folder_color = ''
        else:
            folder_color = f'/{color}'

        if type == 1:
            folder_type = 'walker'
            if var == 1:
                folder_var = '1'
            elif var == 2:
                folder_var = '2'
            else:
                folder_var = '0'
        elif type == 2:
            folder_type = 'lobber'
            if var == 1:
                folder_var = '1'
            elif var == 2:
                folder_var = '2'
            else:
                folder_var = '2'
        else:
            folder_type = 'walker'
            folder_var = '0'


        self.deco = pygame.image.load(f'images/enemies/{folder_type}/{folder_var}{folder_color}/top_deco.png')
        self.image = self.deco
        self.rect = self.image.get_rect(midbottom = self.enemy.rect.midtop)

    def update(self):
        if not self.enemy.alive():
            self.kill()
        self.rect = self.image.get_rect(midbottom = self.enemy.rect.midtop)
        if self.enemy.left: self.image = pygame.transform.flip(self.deco, True, False)
        else: self.image = self.deco