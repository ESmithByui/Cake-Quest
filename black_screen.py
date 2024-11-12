import pygame

class Game_over_load(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.alpha = 0
        self.black = pygame.image.load('images/load_screens/game_over.png').convert_alpha()
        self.image = self.black
        self.rect = self.image.get_rect(topleft = (0,0))
        self.image.set_alpha(self.alpha)
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
            self.image.set_alpha(self.alpha)