import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_w, screen_h):
        super().__init__()
        surf = pygame.image.load('images/player/8bit_slime.png').convert_alpha()
        self.player_walk = surf
        self.image = self.player_walk
        self.rect = self.image.get_rect(midbottom = (200, 200))
        self.gravity = 0
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.speed = 6
        self.left = False
        self.in_air = False
        
        #animation
        self.animation_index = 0
        self.invincible_image = pygame.image.load('images/player/8bit_slime_inv.png')
        idle_0 = pygame.image.load('images/player/8bit_slime_idle_0.png')
        idle_1 = pygame.image.load('images/player/8bit_slime_idle_1.png')
        self.idle_frames = [idle_0, idle_0, idle_0, idle_0, idle_0, idle_0, idle_0, idle_0, idle_0, idle_0, idle_1, idle_1]
        walk_0 = pygame.image.load('images/player/8bit_slime_walk_0.png')
        walk_1 = pygame.image.load('images/player/8bit_slime_walk_1.png')
        self.walk_frames = [walk_0, walk_1]
        jump_0 = pygame.image.load('images/player/8bit_slime_jump_0.png')
        jump_1 = pygame.image.load('images/player/8bit_slime_jump_1.png')
        self.jump_frames = [jump_0, jump_1]
        fall_0 = pygame.image.load('images/player/8bit_slime_fall_0.png')
        fall_1 = pygame.image.load('images/player/8bit_slime_fall_1.png')
        self.fall_frames = [fall_0, fall_1]
        attack_0 = pygame.image.load('images/player/8bit_slime_attack_0.png')
        attack_1 = pygame.image.load('images/player/8bit_slime_attack_1.png')
        attack_2 = pygame.image.load('images/player/8bit_slime_attack_2.png')
        attack_3 = pygame.image.load('images/player/8bit_slime_attack_3.png')
        attack_4 = pygame.image.load('images/player/8bit_slime_attack_4.png')
        self.attack_frames = [attack_0,attack_1,attack_2,attack_3,attack_4,attack_4]
        crouch = pygame.image.load('images/player/8bit_slime_squish.png')   
        self.crouch_frames = [crouch]
        self.animation_frames = self.idle_frames


        #attacks
        self.throw_projectile = False
        self.attack_cooldown = 0
        self.attack = False
        self.attack_type = 0
        self.attack_index = 0
        self.test_list = [1,2,3,4,5,6]

        #health
        self.max_health = 3
        self.health = self.max_health
        self.invincible = False
        self.invincibility_frames = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if not self.attack:
            if keys[pygame.K_q] and self.attack_cooldown <= 0:
                if not self.throw_projectile:
                    self.animation_index = 0
                    self.attack_index = 0
                    self.attack = True
                    self.attack_type = 1
                    self.attack_cooldown = 60
            elif keys[pygame.K_e] and self.attack_cooldown <= 0:
                self.animation_index = 0
                self.attack_index = 0
                self.attack = True
                self.attack_type = 2
                self.attack_cooldown = 30
            elif keys[pygame.K_s]:
                self.animation_frames = self.crouch_frames

            else:
                if keys[pygame.K_w] and not self.in_air:
                    self.gravity = -20
                    self.in_air = True
                if keys[pygame.K_d]:
                    self.rect.x += self.speed
                    self.left = False
                    self.animation_frames = self.walk_frames
                if keys[pygame.K_a]:
                    self.rect.x -= self.speed
                    self.left = True
                    self.animation_frames = self.walk_frames
                if self.rect.left <= 0:
                    self.rect.left = 0
                if self.rect.right >= self.screen_w:
                    self.rect.right = self.screen_w


    def apply_gravity(self):
        if self.in_air:
            self.gravity += 1
            self.rect.y += self.gravity
            if self.gravity >= 49:
                self.gravity = 49
        else:
            self.gravity = 0
        if self.rect.top >= self.screen_h:
            self.rect.bottom = 0
    
    def animation_state(self):
        if self.gravity > 1 and not self.attack:
            self.animation_frames = self.fall_frames
        elif self.gravity < 0 and not self.attack:
            self.animation_frames = self.jump_frames

        if self.attack:
            self.animation_index += 0.5
            if self.animation_index >= len(self.animation_frames): self.animation_index = 0
            self.image = self.animation_frames[int(self.animation_index)]
        else:
            self.animation_index += 0.1
            if self.animation_index >= len(self.animation_frames): self.animation_index = 0
            self.image = self.animation_frames[int(self.animation_index)]
        
        if self.left:
            self.image = pygame.transform.flip(self.image, True, False)
        if self.invincible and (int(self.animation_index) % 2 == 0):
            self.image = self.invincible_image
        self.rect = self.image.get_rect(midbottom = self.rect.midbottom)

    def update(self):
        self.animation_frames = self.idle_frames
        self.player_input()
        self.player_attack()
        self.apply_gravity()
        self.animation_state()
        if self.invincibility_frames > 0:
            self.invincibility_frames -= 1
        else: self.invincible = False

    def player_attack(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        if self.attack:
            self.animation_frames = self.attack_frames
            if self.attack_type == 1:
                self.attack_index += 0.5
                if int(self.attack_index) == 4:
                    self.throw_projectile = True
                if self.attack_index >= len(self.attack_frames):
                    self.attack_index = 0
                    self.attack = False
            if self.attack_type == 2:
                self.attack_index += 0.5
                if self.attack_index >= len(self.attack_frames):
                    self.attack_index = 0
                    self.attack = False

    def damage(self):
        if not self.invincible:
            self.health -= 1
            self.invincibility_frames = 100
            self.invincible = True