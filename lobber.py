import pygame
import random
from enemy_deco import Enemy_deco
from enemy_death import Enemy_death
from float_score import Float_score
from lobber_projectile import Lobber_projectile

class Lobber(pygame.sprite.Sprite):
    def __init__(self, coord, screen_w, screen_h, deco, var, death_animations, projectile_list):
        super().__init__()
        self.image = pygame.image.load('images/enemies/lobber/2/walk_0.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (coord))
        self.death_animations = death_animations
        self.var = var
        self.score = 2
        self.speed = 1
        self.gravity = 0
        

        #attack info
        self.delay = 60
        self.max_extra = 120
        self.projectile_speed_1 = 1
        self.projectile_speed_2 = 3
        self.projectile_speed_3 = 5
        self.cooldown = 100
        self.fired = False
        self.attack_state = False
        self.projectile_list = projectile_list



        variants = ''
        self.color = 0
        

        if var == 1:
            folder = '1'
            if random.randint(0,1) == 1:
                variants = '/1'
                self.color = 1
            deco.add(Enemy_deco(self,2,1))


        elif var == 2:
            folder = '2'
            randint = random.randint(0,2)
            if randint == 1:
                variants = '/1'
                self.color = 1
                deco.add(Enemy_deco(self,2,2,1))
                self.cooldown = 0
                
            elif randint == 2:
                variants = '/2'
                self.color = 2
                deco.add(Enemy_deco(self,2,2,2))
                self.projectile_speed_1 = 2
                self.projectile_speed_2 = 0
                self.projectile_speed_3 = -2

            else:
                deco.add(Enemy_deco(self,2,2))

        else:
            folder = '2'
            deco.add(Enemy_deco(self,2,2))

        walk_0 = pygame.image.load(f'images/enemies/lobber/{folder}{variants}/walk_0.png').convert_alpha()
        walk_1 = pygame.image.load(f'images/enemies/lobber/{folder}{variants}/walk_1.png').convert_alpha()
        walk_2 = pygame.image.load(f'images/enemies/lobber/{folder}{variants}/walk_2.png').convert_alpha()
        attack_1 = pygame.image.load(f'images/enemies/lobber/{folder}{variants}/attack_1.png').convert_alpha()
        attack_2 = pygame.image.load(f'images/enemies/lobber/{folder}{variants}/attack_2.png').convert_alpha()
        self.projectile_image = pygame.image.load(f'images/enemies/lobber/{folder}{variants}/projectile.png').convert_alpha()

        self.frames = [walk_0,walk_1,walk_0,walk_2]
        self.attack_frames = [walk_0,attack_1,attack_2,attack_1,walk_0]
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
        if self.cooldown > 0:
            self.cooldown -= 1
        if self.cooldown <= 0:
            self.attack_state = True
        if self.attack_state:
            self.attack()
        else:
            self.animation_state()
            self.move()
        self.apply_gravity()
        self.destroy()

    def death(self):
        self.death_animations.add(Float_score(self.rect.midbottom, self.score))
        self.death_animations.add(Enemy_death(self.rect.midbottom, self.left ,2, self.var, self.color))
        self.kill()

    def attack(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.attack_frames): 
            self.animation_index = 0
            self.attack_state = False
            self.fired = False
            self.cooldown = self.delay + random.randint(0, self.max_extra)
        if self.animation_index >= 2:
            if not self.fired:
                self.projectile_list.add(Lobber_projectile(self.projectile_image, self.left, self.rect.center,self.screen_w, self.screen_h, self.projectile_speed_1))
                self.projectile_list.add(Lobber_projectile(self.projectile_image, self.left, self.rect.center,self.screen_w, self.screen_h, self.projectile_speed_2))
                self.projectile_list.add(Lobber_projectile(self.projectile_image, self.left, self.rect.center,self.screen_w, self.screen_h, self.projectile_speed_3))
                self.fired = True
        if self.left: self.image = pygame.transform.flip(self.attack_frames[int(self.animation_index)], True, False)
        else: self.image = self.attack_frames[int(self.animation_index)]
        self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
            

