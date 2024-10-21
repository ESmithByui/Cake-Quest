import pygame

class Platform_contructor(pygame.sprite.Sprite):
    def __init__(self, coord, type = 'block'):
        super().__init__()
        if type == ('g_f_b'):
            self.image = pygame.image.load('images/platforms/8bit_grass_floating_block.png').convert_alpha()
        elif type == ('g_f_l'):
            self.image = pygame.image.load('images/platforms/8bit_grass_floating_long.png').convert_alpha()
        elif type == ('g_f_l2'):
            self.image = pygame.transform.flip(pygame.image.load('images/platforms/8bit_grass_floating_long.png').convert_alpha(), True, False)
        elif type == ('g_f_s'):
            self.image = pygame.image.load('images/platforms/8bit_grass_floating_short.png').convert_alpha()
        elif type == ('g_floor'):
            self.image = pygame.image.load('images/platforms/8bit_grass_floor.png').convert_alpha()
        elif type == ('g_p'):
            self.image = pygame.image.load('images/platforms/8bit_grass_pillar.png').convert_alpha()
        elif type == ('s_floor'):
            self.image = pygame.image.load('images/platforms/8bit_stone_floor.png').convert_alpha()
        elif type == ('s_c_wall'):
            self.image = pygame.image.load('images/platforms/8bit_stone_crystal_wall.png').convert_alpha()
        elif type == ('s_c_cieling'):
            self.image = pygame.image.load('images/platforms/8bit_stone_cieling.png').convert_alpha()
        elif type == ('s_center_wall'):
            self.image = pygame.image.load('images/platforms/8bit_stone_center_wall.png').convert_alpha()
        elif type == ('s_c_pillar'):
            self.image = pygame.image.load('images/platforms/8bit_stone_crystal_pillar.png').convert_alpha()
        elif type == ('s_b_p'):
            self.image = pygame.image.load('images/platforms/8bit_stone_blue_platform.png').convert_alpha()
        elif type == ('s_p_p'):
            self.image = pygame.image.load('images/platforms/8bit_stone_pink_platform.png').convert_alpha()
        elif type == ('c_floor'):
            self.image = pygame.image.load('images/platforms/8bit_castle_floor.png').convert_alpha()
        elif type == ('c_center'):
            self.image = pygame.image.load('images/platforms/8bit_castle_center_plat.png').convert_alpha()
        elif type == ('c_s1_l'):
            self.image = pygame.image.load('images/platforms/8bit_castle_stairl_1.png').convert_alpha()
        elif type == ('c_s2_l'):
            self.image = pygame.image.load('images/platforms/8bit_castle_stairl_2.png').convert_alpha()
        elif type == ('c_s3_l'):
            self.image = pygame.image.load('images/platforms/8bit_castle_stairl_3.png').convert_alpha()
        elif type == ('c_s4_l'):
            self.image = pygame.image.load('images/platforms/8bit_castle_stairl_4.png').convert_alpha()
        elif type == ('c_s5_l'):
            self.image = pygame.image.load('images/platforms/8bit_castle_stairl_5.png').convert_alpha()
        elif type == ('c_s1_r'):
            self.image = pygame.image.load('images/platforms/8bit_castle_stairr_1.png').convert_alpha()
        elif type == ('c_s2_r'):
            self.image = pygame.image.load('images/platforms/8bit_castle_stairr_2.png').convert_alpha()
        elif type == ('c_s3_r'):
            self.image = pygame.image.load('images/platforms/8bit_castle_stairr_3.png').convert_alpha()
        elif type == ('c_s4_r'):
            self.image = pygame.image.load('images/platforms/8bit_castle_stairr_4.png').convert_alpha()
        elif type == ('c_s5_r'):
            self.image = pygame.image.load('images/platforms/8bit_castle_stairr_5.png').convert_alpha()
        elif type == ('c_table'):
            self.image = pygame.image.load('images/platforms/8bit_castle_table.png').convert_alpha()
        else:
            self.image = pygame.image.load('images/platforms/8bit_grass.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = coord)
