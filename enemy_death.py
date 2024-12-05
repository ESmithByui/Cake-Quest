import pygame

class Enemy_death(pygame.sprite.Sprite):
    def __init__(self, coord, dir, type, var, color = 0):
        super().__init__()
        self.left = dir
        self.animation_index = 0

        if color == 0:
            folder_color = ''
        else:
            folder_color = f'/{color}'

        if type == 1:
            folder_type = 'walker'
            if var == 1:
                folder_var = '1'
            elif var == 2:
                folder_var = '2'
            
            else:
                folder_var = '1'

        elif type == 2:
            folder_type = 'lobber'
            if var == 1:
                folder_var = '1'
            elif var == 2:
                folder_var = '2'
            
            else:
                folder_var = '2'
                
        else:
            folder_type = 'walker'
            folder_var = '1'
            
        death_0 = pygame.image.load(f'images/enemies/{folder_type}/{folder_var}{folder_color}/death_0.png').convert_alpha()
        death_1 = pygame.image.load(f'images/enemies/{folder_type}/{folder_var}{folder_color}/death_1.png').convert_alpha()
        death_2 = pygame.image.load(f'images/enemies/{folder_type}/{folder_var}{folder_color}/death_2.png').convert_alpha()
        death_3 = pygame.image.load(f'images/enemies/{folder_type}/{folder_var}{folder_color}/death_3.png').convert_alpha()
        death_4 = pygame.image.load(f'images/enemies/{folder_type}/{folder_var}{folder_color}/death_4.png').convert_alpha()
        death_5 = pygame.image.load(f'images/enemies/{folder_type}/{folder_var}{folder_color}/death_5.png').convert_alpha()
        death_6 = pygame.image.load(f'images/enemies/{folder_type}/{folder_var}{folder_color}/death_6.png').convert_alpha()

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
