import pygame

class Health_bar():
    def __init__(self, screen, x, y, player):

        self.player = player
        self.screen = screen
        self.x = x
        self.y = y
        self.spacer = 50
        self.pieces = []
        for i in range(self.player.max_health):
            self.pieces.append(Health_piece((i * self.spacer + self.x, self.y), self.screen))

    def update(self):
        if len(self.pieces) < self.player.max_health:
            self.pieces.clear()
            for i in range(self.player.max_health):
                self.pieces.append(Health_piece((i * self.spacer + self.x, self.y), self.screen))
        
        current = self.player.health
        for piece in self.pieces:
            if current > 0:
                piece.full = True
                current -= 1
            else: piece.full = False



    def draw(self):
        self.update()
        for piece in self.pieces:
            piece.draw()



class Health_piece():
    def __init__(self, coord, screen):
        self.coord = coord
        self.full = True
        hp_full_1 = pygame.image.load('images/hp_bar/hp_bar_1.png')
        hp_full_2 = pygame.image.load('images/hp_bar/hp_bar_2.png')
        hp_full_3 = pygame.image.load('images/hp_bar/hp_bar_3.png')
        self.hp_full_frames = [hp_full_1,hp_full_2,hp_full_3]
        hp_empty_1 = pygame.image.load('images/hp_bar/hp_bar_empty_1.png')
        hp_empty_2 = pygame.image.load('images/hp_bar/hp_bar_empty_2.png')
        hp_empty_3 = pygame.image.load('images/hp_bar/hp_bar_empty_3.png')
        self.hp_empty_frames = [hp_empty_1,hp_empty_2,hp_empty_3]
        self.screen = screen

        self.animation_index = 0
        self.image = self.hp_full_frames[self.animation_index]
        self.rect = self.image.get_rect(topleft = coord)

    def animation_state(self):
        self.animation_index += 0.1
        if self.full: frames = self.hp_full_frames
        else: frames = self.hp_empty_frames
        if self.animation_index >= len(frames): self.animation_index = 0
        self.image = frames[int(self.animation_index)]
    
    def draw(self):
        self.animation_state()
        self.screen.blit(self.image, self.rect)
