import pygame

class Foreground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.default = pygame.image.load('images/backgrounds/empty_foreground.png').convert_alpha()
        self.level_1_foreground = pygame.image.load('images/backgrounds/level_1_foreground.png').convert_alpha()
        self.level_2_foreground = pygame.image.load('images/backgrounds/level_2_foreground.png').convert_alpha()
        self.level_final_foreground = pygame.image.load('images/backgrounds/level_final_foreground.png').convert_alpha()

        self.image = self.level_1_foreground
        self.rect = self.image.get_rect(topleft = (0,0))

    def update(self, level):
        if level == 1:
            self.image = self.level_1_foreground
        elif level == 2:
            self.image = self.level_2_foreground
        elif level == -10:
            self.image = self.level_final_foreground
        else: 
            self.image = self.default