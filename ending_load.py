import pygame

class End_load(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.alpha = 0
        self.white = pygame.image.load('images/load_screens/end_white.png').convert_alpha()
        self.image = self.white
        self.rect = self.image.get_rect(topleft = (0,0))
        self.change = 1
        self.active = False

    def update(self):
        if self.active:
            self.alpha += self.change
            if self.alpha > 255:
                self.alpha = 255
                self.change = -self.change
            if self.alpha < 0:
                self.alpha = 0
                self.active = False
                self.change = -self.change
            self.image.fill((255,255,255, self.alpha))
    