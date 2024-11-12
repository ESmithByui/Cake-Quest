import pygame
import random
from walker import Walker

class Spawner(pygame.sprite.Sprite):
    def __init__(self, coord, screen_w, screen_h, enemies, deco, enemy_list, var = 0):
        super().__init__()
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.enemies = enemies
        self.deco = deco
        self.var = var
        self.enemy_list = enemy_list
        self.spawned = False

        if self.var == 1:
            self.active = pygame.image.load('images/spawner/1/active.png').convert_alpha()
            self.inactive = pygame.image.load('images/spawner/1/inactive.png').convert_alpha()
            alert_1 = pygame.image.load('images/spawner/1/alert_1.png').convert_alpha()
            alert_2 = pygame.image.load('images/spawner/1/alert_2.png').convert_alpha()
            alert_3 = pygame.image.load('images/spawner/1/alert_3.png').convert_alpha()
        else:
            self.active = pygame.image.load('images/spawner/1/active.png').convert_alpha()
            self.inactive = pygame.image.load('images/spawner/1/inactive.png').convert_alpha()
            alert_1 = pygame.image.load('images/spawner/1/alert_1.png').convert_alpha()
            alert_2 = pygame.image.load('images/spawner/1/alert_2.png').convert_alpha()
            alert_3 = pygame.image.load('images/spawner/1/alert_3.png').convert_alpha()

        self.image = self.inactive
        self.rect = self.image.get_rect(midbottom = coord)
        self.cooldown = 0
        self.animation_index = 0
        self.frames = [alert_1, alert_2, alert_3,alert_1, alert_2, alert_3,alert_1, alert_2, alert_3]

    def update(self):
        if self.cooldown > 0:
            if not self.spawned:
                self.animation_state()
            self.cooldown -= 1
        else:
            self.image = self.inactive
            self.animation_index = 0
        
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): 
            self.animation_index = len(self.frames)
            self.image = self.active
            self.spawn()
        else:
            self.image = self.frames[int(self.animation_index)]


    def spawn(self):
        enemy = random.choice(self.enemy_list)
        if enemy == 'walker':
            self.enemies.add(Walker(self.rect.midbottom, self.screen_w, self.screen_h, self.deco, self.var))
        self.spawned = True
            
    def activate(self):
        if not self.cooldown > 0:
            self.cooldown = 500
            self.spawned = False
    