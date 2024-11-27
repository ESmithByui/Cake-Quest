import pygame
import random
from enemy_deco import Enemy_deco
from enemy_death import Enemy_death
from float_score import Float_score

class Walker(pygame.sprite.Sprite):
    def __init__(self, coord, screen_w, screen_h, deco, var, death_animations):
        super().__init__()
        self.image = pygame.image.load('images/enemies/walker/0/walk_0.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (coord))
        self.death_animations = death_animations
        self.var = var
        self.score = 1

        if var == 1:
            walk_0 = pygame.image.load('images/enemies/walker/1/walk_0.png').convert_alpha()
            walk_1 = pygame.image.load('images/enemies/walker/1/walk_1.png').convert_alpha()
            walk_2 = pygame.image.load('images/enemies/walker/1/walk_2.png').convert_alpha()
            deco.add(Enemy_deco(self,1,1))
            self.speed = 2

        else:
            walk_0 = pygame.image.load('images/enemies/walker/0/walk_0.png').convert_alpha()
            walk_1 = pygame.image.load('images/enemies/walker/0/walk_1.png').convert_alpha()
            walk_2 = pygame.image.load('images/enemies/walker/0/walk_2.png').convert_alpha()
            deco.add(Enemy_deco(self,1,0))
            self.speed = 2


        self.frames = [walk_0,walk_1,walk_0,walk_2]
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (coord))
        self.gravity = 0
        self.screen_w = screen_w
        self.screen_h = screen_h
        choices = [True, False]
        self.left = random.choice(choices)
        self.in_air = False

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

    def death(self):
        self.death_animations.add(Float_score(self.rect.midbottom, self.score))
        self.death_animations.add(Enemy_death(self.rect.midbottom,1, self.var, self.left))
        self.kill()

    
