import pygame

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self, font, screen_w, screen_h):
        super().__init__()
        self.score = 0
        self.font = font
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.image = self.font.render(f'Score: {self.score}',False,('Black'))
        self.rect = self.image.get_rect(topright = (screen_w - 10, 10))

    def update(self):
        self.image = self.font.render(f'Score: {self.score}',False,('Black'))
        self.rect = self.image.get_rect(topright = (self.screen_w - 10, 10))
        


    def add_score(self):
        self.score += 1
    
