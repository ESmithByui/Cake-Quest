import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.default = pygame.image.load('images/backgrounds/wip.png')
        self.main_menu = pygame.image.load('images/backgrounds/main_menu.png')
        self.level_1_background = pygame.image.load('images/backgrounds/level_1_background.png')
        self.level_2_background = pygame.image.load('images/backgrounds/level_2_background.png')
        self.level_final_background = pygame.image.load('images/backgrounds/level_final_background.png')
        self.win_screen = pygame.image.load('images/backgrounds/win_screen.png')


        self.image = self.main_menu
        self.rect = self.image.get_rect(topleft = (0,0))

    def update(self, level):
        if level == 0:
            self.image = self.main_menu
        elif level == 1:
            self.image = self.level_1_background
        elif level == 2:
            self.image = self.level_2_background
        elif level == -10:
            self.image = self.level_final_background
        elif level == -9:
            self.image = self.win_screen
        else: 
            self.image = self.default