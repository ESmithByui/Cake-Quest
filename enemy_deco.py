import pygame
import random

class Enemy_deco(pygame.sprite.Sprite):
    def __init__(self, enemy, type, var):
        super().__init__()
        self.enemy = enemy

        if type == 1:
            if var == 1:
                self.deco = pygame.image.load('images/enemies/walker/1/top_deco.png')
            else:
                self.deco = pygame.image.load('images/enemies/walker/0/top_deco.png')
        else:
            self.deco = pygame.image.load('images/enemies/walker/0/top_deco.png')


        self.image = self.deco
        self.rect = self.image.get_rect(midbottom = self.enemy.rect.midtop)

    def update(self):
        if not self.enemy.alive():
            self.kill()
        self.rect = self.image.get_rect(midbottom = self.enemy.rect.midtop)
        if self.enemy.left: self.image = pygame.transform.flip(self.deco, True, False)
        else: self.image = self.deco