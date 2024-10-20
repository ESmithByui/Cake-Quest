import pygame


class Player_melee(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.melee_standby = pygame.image.load('images/player/cudgel_0.png')
        melee_1 = pygame.image.load('images/player/cudgel_1.png')
        melee_2 = pygame.image.load('images/player/cudgel_2.png')
        melee_3 = pygame.image.load('images/player/cudgel_3.png')
        melee_4 = pygame.image.load('images/player/cudgel_4.png')
        melee_5 = pygame.image.load('images/player/cudgel_5.png')
        self.melee_frames = [self.melee_standby, melee_1,melee_2,melee_3,melee_4,melee_5]
        self.active = False
        self.image = self.melee_standby
        self.rect = self.image.get_rect(midbottom = self.player.rect.midbottom)
        self.animation_index = 0

    def animation_state(self):
        if self.active:
            self.animation_index += 0.5
            if self.animation_index >= len(self.melee_frames):
                self.animation_index = 0
                self.active = False
            if self.player.left:
                self.image = pygame.transform.flip(self.melee_frames[int(self.animation_index)], True, False)
            else:
                self.image = self.melee_frames[int(self.animation_index)]
        else: self.image = self.melee_standby

    def check_active(self):
        if self.player.attack and self.player.attack_type == 2:
            self.active = True

    def update(self):
        self.rect.midbottom = self.player.rect.midbottom
        self.check_active()
        self.animation_state()
    

