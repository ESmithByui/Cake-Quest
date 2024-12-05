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
        self.speed = 2
        self.gravity = 0

        variants = ''
        self.color = 0
        

        if var == 1:
            folder = '1'
            if random.randint(0,1) == 1:
                variants = '/1'
                self.color = 1
            deco.add(Enemy_deco(self,1,1))


        elif var == 2:
            folder = '2'
            randint = random.randint(0,2)
            if randint == 1:
                variants = '/1'
                self.color = 1
                deco.add(Enemy_deco(self,1,2,1))
                self.gravity = 100
                
            elif randint == 2:
                variants = '/2'
                self.color = 2
                deco.add(Enemy_deco(self,1,2,2))
                self.speed = 1
            else:
                deco.add(Enemy_deco(self,1,2))

        else:
            folder = '0'
            deco.add(Enemy_deco(self,1,0))

        walk_0 = pygame.image.load(f'images/enemies/walker/{folder}{variants}/walk_0.png').convert_alpha()
        walk_1 = pygame.image.load(f'images/enemies/walker/{folder}{variants}/walk_1.png').convert_alpha()
        walk_2 = pygame.image.load(f'images/enemies/walker/{folder}{variants}/walk_2.png').convert_alpha()

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
        self.death_animations.add(Enemy_death(self.rect.midbottom, self.left ,1, self.var, self.color))
        self.kill()

    
