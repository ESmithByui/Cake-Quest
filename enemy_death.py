import pygame

class Enemy_death(pygame.sprite.Sprite):
    def __init__(self, coord, type, var, dir):
        super().__init__()
        self.left = dir
        self.animation_index = 0

        if type == 1:
            if var == 1:
                death_0 = pygame.image.load('images/enemies/walker/1/death_0.png').convert_alpha()
                death_1 = pygame.image.load('images/enemies/walker/1/death_1.png').convert_alpha()
                death_2 = pygame.image.load('images/enemies/walker/1/death_2.png').convert_alpha()
                death_3 = pygame.image.load('images/enemies/walker/1/death_3.png').convert_alpha()
                death_4 = pygame.image.load('images/enemies/walker/1/death_4.png').convert_alpha()
                death_5 = pygame.image.load('images/enemies/walker/1/death_5.png').convert_alpha()
                death_6 = pygame.image.load('images/enemies/walker/1/death_6.png').convert_alpha()
            else:
                death_0 = pygame.image.load('images/enemies/walker/1/death_0.png').convert_alpha()
                death_1 = pygame.image.load('images/enemies/walker/1/death_1.png').convert_alpha()
                death_2 = pygame.image.load('images/enemies/walker/1/death_2.png').convert_alpha()
                death_3 = pygame.image.load('images/enemies/walker/1/death_3.png').convert_alpha()
                death_4 = pygame.image.load('images/enemies/walker/1/death_4.png').convert_alpha()
                death_5 = pygame.image.load('images/enemies/walker/1/death_5.png').convert_alpha()
                death_6 = pygame.image.load('images/enemies/walker/1/death_6.png').convert_alpha()
        else:
            death_0 = pygame.image.load('images/enemies/walker/1/death_0.png').convert_alpha()
            death_1 = pygame.image.load('images/enemies/walker/1/death_1.png').convert_alpha()
            death_2 = pygame.image.load('images/enemies/walker/1/death_2.png').convert_alpha()
            death_3 = pygame.image.load('images/enemies/walker/1/death_3.png').convert_alpha()
            death_4 = pygame.image.load('images/enemies/walker/1/death_4.png').convert_alpha()
            death_5 = pygame.image.load('images/enemies/walker/1/death_5.png').convert_alpha()
            death_6 = pygame.image.load('images/enemies/walker/1/death_6.png').convert_alpha()

        self.frames = [death_0,death_1,death_2,death_3,death_4,death_5,death_6]
        self.image = self.frames[int(self.animation_index)]
        if self.left: self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect(midbottom = coord)


    def update(self):
        self.animation_index += 0.2
        if self.animation_index >= len(self.frames): 
            self.kill()
            self.animation_index -= 1
        self.image = self.frames[int(self.animation_index)]
        if self.left: self.image = pygame.transform.flip(self.image, True, False)
