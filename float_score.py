import pygame

class Float_score(pygame.sprite.Sprite):
    def __init__(self, coord, score):
        super().__init__()
        self.left = dir
        self.animation_index = 0

        if score == 1:
            self.image = pygame.image.load('images/enemies/scores/1.png').convert_alpha()
        elif score == 2:
            self.image = pygame.image.load('images/enemies/scores/2.png').convert_alpha()
            
        else:
            self.image = pygame.image.load('images/enemies/scores/1.png').convert_alpha()

        self.rect = self.image.get_rect(midbottom = coord)


    def update(self):
        self.animation_index += 5
        self.rect.y -= 2
        if self.animation_index >= (255): 
            self.kill()
        self.image.set_alpha(255 - self.animation_index)
