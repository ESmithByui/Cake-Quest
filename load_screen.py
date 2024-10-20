import pygame

class Load_screen(pygame.sprite.Sprite):
    def __init__(self, screen_h):
        super().__init__()
        self.screen_h = screen_h
        #font size 72 paint.net
        self.load_basic = pygame.image.load('images/load_screens/loading_basic.png')
        self.load_1 = pygame.image.load('images/load_screens/load_level_1.png')
        self.load_2 = pygame.image.load('images/load_screens/load_level_2.png')
        self.load_final = pygame.image.load('images/load_screens/load_level_final.png')
        self.image = self.load_1
        self.rect = self.image.get_rect(bottomleft = (0,-5))
        self.speed = 0
        self.downtime = -1
        self.load = False
        self.active = False
        self.state = 0
        


    def update(self):
        self.rect.y += self.speed
        if self.downtime > 0:
            self.speed = 0
            self.downtime -= 1
        elif self.downtime == 0:
            self.speed = -10
            self.load = False
            self.downtime = -1

        if self.rect.bottom > self.screen_h:
            self.rect.bottom = self.screen_h
            self.speed = 0
            self.downtime = 180
            self.load = True
            self.state = 1
        elif self.rect.bottom < 0 and self.speed < 0:
            self.rect.bottom = -10
            self.speed = 0
            self.active = False

    def prep(self, level):
        if level == 1:
            self.image = self.load_1
        elif level == 2:
            self.image = self.load_2
        elif level == -10:
            self.image = self.load_final
        else:
            self.image = self.load_basic
        self.active = True
        self.speed = 10
        self.state = 0
