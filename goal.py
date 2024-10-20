import pygame

class Goal(pygame.sprite.Sprite):
    def __init__(self, coord):
        super().__init__()
        self.image = pygame.image.load('images/food/full_cake.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = coord)
