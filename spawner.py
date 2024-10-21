import pygame
import random
from roller import Roller

class Spawner(pygame.sprite.Sprite):
    def __init__(self, coord, screen_w, screen_h):
        super().__init__()
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.g_den_inactive = pygame.image.load('images/spawner/g_spawner_1.png').convert_alpha()
        self.g_den_active = pygame.image.load('images/spawner/g_spawner_2.png').convert_alpha()
        self.image = self.g_den_inactive
        self.rect = self.image.get_rect(midbottom = coord)
        self.cooldown = 0
        self.enemy_types = ['roller']

    def update(self):
        if self.cooldown > 0:
            self.image = self.g_den_active
            self.cooldown -= 1
        else:
            self.image = self.g_den_inactive
        

    def spawn(self, enemies):
        if self.cooldown <= 0:
            enemy = random.choice(self.enemy_types)
            self.cooldown = 500
            if enemy == 'roller':
                enemies.add(Roller(self.rect.midbottom, self.screen_w, self.screen_h))
            

    