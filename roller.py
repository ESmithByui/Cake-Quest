import pygame
import random
from enemy_deco import Enemy_deco

class Roller(pygame.sprite.Sprite):
    def __init__(self, coord, screen_w, screen_h, deco):
        super().__init__()
        roller_1 = pygame.image.load('images/roller/r_roller_1.png').convert_alpha()
        roller_2 = pygame.image.load('images/roller/r_roller_2.png').convert_alpha()


        test_walk_0 = pygame.image.load('images/enemy/test_enemy_walk_0.png').convert_alpha()
        test_walk_1 = pygame.image.load('images/enemy/test_enemy_walk_1.png').convert_alpha()
        test_walk_2 = pygame.image.load('images/enemy/test_enemy_walk_2.png').convert_alpha()
        self.frames = [test_walk_0,test_walk_1,test_walk_0,test_walk_2]
        #self.frames = [roller_1,roller_2]
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (coord))
        self.gravity = 0
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.speed = 2
        choices = [True, False]
        self.left = random.choice(choices)
        self.in_air = False

        deco.add(Enemy_deco(self))

    def apply_gravity(self):
        if self.in_air:
            self.gravity += 1
            self.rect.y += self.gravity
            if self.gravity >= 20:
                self.gravity = 20
        else:
            self.gravity = 0

    def destroy(self):
        if self.rect.top >= self.screen_h:
            self.kill()
    
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        if self.left: self.image = pygame.transform.flip(self.frames[int(self.animation_index)], True, False)
        else: self.image = self.frames[int(self.animation_index)]
        self.rect = self.image.get_rect(midbottom = self.rect.midbottom)

    def move(self):
        if self.rect.left <= 0:
            self.rect.left = 0
            self.left = False
        if self.rect.right >= self.screen_w:
            self.rect.right = self.screen_w
            self.left = True

        if self.left:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

    def update(self):
        self.animation_state()
        self.move()
        self.apply_gravity()
        self.destroy()
