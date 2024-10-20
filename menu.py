import pygame

class Menu():
    def __init__(self, font, screen_w, screen_h, screen, scoreboard, player):
        self.font = font
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.screen = screen
        self.scoreboard = scoreboard
        self.player = player
        self.text = 'Cake Quest'
        self.image = self.font.render(self.text, False, ('Black'))
        self.rect = self.image.get_rect(midbottom = (screen_w//2, 200))
        self.options = []
        self.options.append(Menu_option(self.font, (screen_w//2, 400), 'Play', self.screen))
        self.options.append(Menu_option(self.font, (screen_w//2,550), 'Quit',self.screen))

    def draw(self):
        self.image = pygame.transform.scale2x(self.font.render(self.text, False, ('Black')))
        self.rect = self.image.get_rect(midbottom = (self.screen_w//2, 200))
        if self.player.health <= 0:
            score_image = self.font.render(f'Score: {self.scoreboard.score}', False, ('Black'))
            score_rect = score_image.get_rect(midtop = (self.screen_w//2,200),)
            self.screen.blit(score_image, score_rect)
        self.screen.blit(self.image, self.rect)
        clicked = pygame.mouse.get_pressed()[0]
        mx, my = pygame.mouse.get_pos()
        
        for option in self.options:
            option.draw(clicked, mx, my)



    

class Menu_option():
    def __init__(self, font, coord, text, screen):
        self.font = font
        self.text = text
        self.screen = screen
        self.coord = coord
        self.image = self.font.render(text, False, ('Black'))
        self.rect = self.image.get_rect(midbottom = coord)
        self.highlight = False
        self.active = False
        self.color = '#45D854'
        self.hcolor = '#89FF97'

    def update(self,mx, my, clicked):
        if self.rect.collidepoint(mx, my):
            self.highlight = True
        else: self.highlight = False
        if self.highlight and clicked:
            self.active = True
        else: self.active = False

    def draw(self, clicked, mx, my):
        self.image = self.font.render(self.text, False, ('Black'))
        self.rect = self.image.get_rect(midbottom = self.coord)
        if self.highlight:
            pygame.draw.rect(self.screen, self.hcolor, self.rect, 0, 15)
        else: pygame.draw.rect(self.screen, self.color, self.rect, 0, 15)
        pygame.draw.rect(self.screen, '#003F06', self.rect, 3, 15)
        self.update(mx, my, clicked)
        self.screen.blit(self.image, self.rect)
        



    
