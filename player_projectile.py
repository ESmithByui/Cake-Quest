import pygame

class Player_projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()

        slime_ball_0 = pygame.image.load('images/player/slime_ball_0.png').convert_alpha()
        slime_ball_1 = pygame.image.load('images/player/slime_ball_1.png').convert_alpha()
        slime_ball_2 = pygame.image.load('images/player/slime_ball_2.png').convert_alpha()
        slime_ball_3 = pygame.image.load('images/player/slime_ball_3.png').convert_alpha()
        self.animation_frames = [slime_ball_0,slime_ball_1,slime_ball_2,slime_ball_3]
        self.image = self.animation_frames[0]
        self.animation_index = 0

        self.rect = self.image.get_rect(center = player.rect.center)
        self.left = player.left
        self.screen_w = player.screen_w
        self.screen_h = player.screen_h
        self.speed = 8
        self.gravity = -10
        
    def apply_movement(self):
        if self.left:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        self.gravity += .5
        self.rect.y += int(self.gravity)
        
    def destroy(self):
        if self.rect.left <= 0:
            self.kill()
        if self.rect.right >= self.screen_w:
            self.kill()
        if self.rect.top >= self.screen_h:
            self.kill()

    def update(self):
        self.apply_movement()
        self.animation()
        self.destroy()

    def animation(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.animation_frames): self.animation_index = 0
        self.image = self.animation_frames[int(self.animation_index)]
        if self.left:
            self.image = pygame.transform.flip(self.image, True, False)