import pygame

class Lobber_projectile(pygame.sprite.Sprite):
    def __init__(self, image, dir, coord, screen_w, screen_h, speed):
        super().__init__()

        self.image = image
        self.left = dir

        self.rect = self.image.get_rect(center = coord)
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.speed = speed
        self.gravity = -10
        self.score = 0
        
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
        self.destroy()

    def death(self):
        self.kill()