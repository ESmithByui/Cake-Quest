import pygame
import random
from sys import exit
from menu import Menu
from scoreboard import Scoreboard
from background import Background
from foreground import Foreground
from load_screen import Load_screen
from ending_load import End_load
from black_screen import Game_over_load
from player import Player
from player_projectile import Player_projectile
from player_melee import Player_melee
from health_bar import Health_bar
from spawner import Spawner
from platform_contrustor import Platform_contructor
from goal import Goal





def block_collision(object, platform):
    platform_touch_list = pygame.sprite.spritecollide(object, platform, False)
    if platform_touch_list:
        for platform in platform_touch_list:
            if object.rect.bottom == platform.rect.top:
                object.in_air = False
                object.rect.bottom = platform.rect.top
            elif object.rect.bottom <= platform.rect.top or object.rect.left <= platform.rect.right or object.rect.right >= platform.rect.left or object.rect.top >= platform.rect.bottom:
                up = abs(object.rect.bottom - platform.rect.top)
                left = abs(object.rect.right - platform.rect.left)
                right = abs(object.rect.left - platform.rect.right)
                down = abs(object.rect.top - platform.rect.bottom)
                movement = min(up, left, right, down)
                if movement == up:
                    object.rect.bottom = platform.rect.top
                    object.in_air = False
                elif movement == left:
                    object.rect.right = platform.rect.left
                elif movement == right:
                    object.rect.left = platform.rect.right
                elif movement == down:
                    object.rect.top = platform.rect.bottom
                    object.gravity = 0
    else:
        object.in_air = True

def eblock_collision(object, platform):
    platform_touch_list = pygame.sprite.spritecollide(object, platform, False)
    if platform_touch_list:
        for platform in platform_touch_list:
            if object.rect.bottom == platform.rect.top:
                object.in_air = False
                object.rect.bottom = platform.rect.top
            elif object.rect.bottom <= platform.rect.top or object.rect.left <= platform.rect.right or object.rect.right >= platform.rect.left or object.rect.top >= platform.rect.bottom:
                up = abs(object.rect.bottom - platform.rect.top)
                left = abs(object.rect.right - platform.rect.left)
                right = abs(object.rect.left - platform.rect.right)
                down = abs(object.rect.top - platform.rect.bottom)
                movement = min(up, left, right, down)
                if movement == up:
                    object.rect.bottom = platform.rect.top
                    object.in_air = False
                elif movement == left:
                    object.rect.right = platform.rect.left
                    object.left = True
                elif movement == right:
                    object.rect.left = platform.rect.right
                    object.left = False
                elif movement == down:
                    object.rect.top = platform.rect.bottom
                    object.gravity = 0

    else:
        object.in_air = True

def projectile_collision(platforms, projectiles):
    for platform in platforms:
        pygame.sprite.spritecollide(platform, projectiles, True)

def player_projectile_collision(enemies, projectiles, score):
    for enemy in enemies:
        if pygame.sprite.spritecollide(enemy, projectiles, True):
            score.add_score(enemy.score)
            enemy.death()

def player_melee_collision(melee, enemies, score):
    if melee.active and melee.animation_index >= 3:
        enemy_list = pygame.sprite.spritecollide(melee, enemies, False)
        for enemy in enemy_list:
            score.add_score(enemy.score)
            enemy.death()

def player_take_melee(player, enemies):
    if pygame.sprite.spritecollide(player, enemies, False):
        player.damage()

def spawner_active(spawners):
    sprite_list = spawners.sprites()
    if len(sprite_list) > 1:
        random.choice(sprite_list).activate()

def load_level_1(player, player_projectiles, enemies, e_deco, death_animations, e_projectiles, platforms, spawners, screen_w, screen_h, background, foreground, goal):
    player_projectiles.empty()
    e_deco.empty()
    enemies.empty()
    death_animations.empty()
    platforms.empty()
    spawners.empty()
    goal.empty()
    player.rect.midbottom = (600,350)
    player.reset()
    
    background.update(1)
    foreground.update(1)

    #platforms
    #base floor
    platforms.add(Platform_contructor((600,800), 'g_floor'))
    platforms.add(Platform_contructor((600,800), 'g_p'))
    #1st floor
    platforms.add(Platform_contructor((200,500), 'g_f_l'))
    platforms.add(Platform_contructor((1000,500), 'g_f_l2'))
    #1st floor blocks
    platforms.add(Platform_contructor((425,550), 'g_f_b'))
    platforms.add(Platform_contructor((775,550), 'g_f_b'))
    #2nd floor platform
    platforms.add(Platform_contructor((600,400), 'g_f_s'))
    #3rd floor
    platforms.add(Platform_contructor((200,275), 'g_f_l'))
    platforms.add(Platform_contructor((1000,275), 'g_f_l2'))


    #spawners
    enemy_list = ['walker']
    spawners.add(Spawner((200,225), screen_w, screen_h, enemies, e_deco, enemy_list, death_animations, e_projectiles, 1))
    spawners.add(Spawner((1000,225), screen_w, screen_h, enemies, e_deco, enemy_list, death_animations, e_projectiles, 1))
    spawners.add(Spawner((200,450), screen_w, screen_h, enemies, e_deco, enemy_list, death_animations, e_projectiles, 1))
    spawners.add(Spawner((1000,450), screen_w, screen_h, enemies, e_deco, enemy_list, death_animations, e_projectiles, 1))

def load_level_2(player, player_projectiles, enemies, e_deco, death_animations, e_projectiles, platforms, spawners, screen_w, screen_h, background, foreground):
    player_projectiles.empty()
    e_deco.empty()
    enemies.empty()
    death_animations.empty()
    platforms.empty()
    spawners.empty()
    player.rect.midbottom = (875,500)

    background.update(2)
    foreground.update(2)

    #platforms
    #cage
    platforms.add(Platform_contructor((600,800),'s_floor'))
    platforms.add(Platform_contructor((25,800),'s_c_wall'))
    platforms.add(Platform_contructor((1175,800),'s_c_wall'))
    platforms.add(Platform_contructor((600,50),'s_c_cieling'))


    platforms.add(Platform_contructor((675,650),'s_center_wall'))
    platforms.add(Platform_contructor((1050,800),'s_c_pillar'))
    platforms.add(Platform_contructor((875,550),'s_b_p'))
    platforms.add(Platform_contructor((975,375),'s_b_p'))
    platforms.add(Platform_contructor((875,200),'s_p_p'))



    #spawners
    enemy_list = ['walker','walker','walker','walker','walker','walker','walker','walker','walker','lobber']
    spawners.add(Spawner((700,150), screen_w, screen_h, enemies, e_deco, enemy_list, death_animations, e_projectiles, 2))
    spawners.add(Spawner((800,150), screen_w, screen_h, enemies, e_deco, enemy_list, death_animations, e_projectiles, 2))
    spawners.add(Spawner((900,150), screen_w, screen_h, enemies, e_deco, enemy_list, death_animations, e_projectiles, 2))
    spawners.add(Spawner((1000,150), screen_w, screen_h, enemies, e_deco, enemy_list, death_animations, e_projectiles, 2))
    spawners.add(Spawner((100,750), screen_w, screen_h, enemies, e_deco, ['lobber'], death_animations, e_projectiles, 2))
    spawners.add(Spawner((1100,650), screen_w, screen_h, enemies, e_deco, enemy_list, death_animations, e_projectiles, 2))

def load_level_end(player, player_projectiles, enemies, e_deco, death_animations, e_projectiles, platforms, spawners, screen_w, screen_h, background, foreground, goal):
    player_projectiles.empty()
    e_deco.empty()
    enemies.empty()
    death_animations.empty()
    platforms.empty()
    spawners.empty()
    player.rect.midbottom = (600,750)

    background.update(-10)
    foreground.update(-10)

    #platforms
    #cage
    platforms.add(Platform_contructor((600,800),'c_floor'))
    platforms.add(Platform_contructor((600,450),'c_center'))
    platforms.add(Platform_contructor((600,400),'c_table'))
    platforms.add(Platform_contructor((200,750),'c_s1_l'))
    platforms.add(Platform_contructor((175,700),'c_s2_l'))
    platforms.add(Platform_contructor((150,650),'c_s3_l'))
    platforms.add(Platform_contructor((125,600),'c_s4_l'))
    platforms.add(Platform_contructor((100,550),'c_s5_l'))
    platforms.add(Platform_contructor((1000,750),'c_s1_r'))
    platforms.add(Platform_contructor((1025,700),'c_s2_r'))
    platforms.add(Platform_contructor((1050,650),'c_s3_r'))
    platforms.add(Platform_contructor((1075,600),'c_s4_r'))
    platforms.add(Platform_contructor((1100,550),'c_s5_r'))

    goal.add(Goal((600,350)))
    




    
    
    

    

    




pygame.init()
screen_w = 1200
screen_h = 800
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption('Cake Quest')
pygame.display.set_icon(pygame.image.load('images/player/8bit_square_slime_icon.png').convert_alpha())
clock = pygame.time.Clock()
font = pygame.font.Font('fonts/slkscr.ttf',50)

player = pygame.sprite.GroupSingle()
player.add(Player(screen_w,screen_h))

player_melee = pygame.sprite.GroupSingle()
player_melee.add(Player_melee(player.sprite))

player_projectiles = pygame.sprite.Group()

score = pygame.sprite.GroupSingle()
score.add(Scoreboard(font, screen_w, screen_h))

hp_bar = Health_bar(screen, 10, 10, player.sprite)

background = pygame.sprite.GroupSingle()
background.add(Background())
foreground = pygame.sprite.GroupSingle()
foreground.add(Foreground())

spawners = pygame.sprite.Group()

enemies = pygame.sprite.Group()
e_deco = pygame.sprite.Group()
e_death_animations = pygame.sprite.Group()
e_projectiles = pygame.sprite.Group()

platforms = pygame.sprite.Group()

goal = pygame.sprite.GroupSingle()

pause_screen = pygame.image.load('images/paused.png').convert_alpha()
pause_rect = pause_screen.get_rect(topleft = (0,0))



menu = Menu(font, screen_w, screen_h, screen, score.sprite, player.sprite)

load_screen = pygame.sprite.GroupSingle()
load_screen.add(Load_screen(screen_h))

end_screen = pygame.sprite.GroupSingle()
end_screen.add(End_load())

game_over = pygame.sprite.GroupSingle()
game_over.add(Game_over_load())

test_background = pygame.Surface((screen_w,screen_h))
test_background.fill('#87CEEB')

test_top_dash = pygame.image.load('images/dash_bar.png').convert_alpha()
test_top_rect = test_top_dash.get_rect(topleft = (0,0))

spawn_timer = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_timer,0)


        
game_active = False
loading = False
level = 0
paused = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == spawn_timer and game_active and not paused and not loading:
            spawner_active(spawners)
        if event.type == pygame.KEYDOWN and game_active and not loading:
            if event.key == pygame.K_ESCAPE:
                if paused:
                    paused = False
                else:
                    paused = True


    #main menu
    if not game_active and not paused:
        pygame.mouse.set_visible(True)
        background.draw(screen)
        if player.sprite.health == 0 or score.sprite.score == 0:
            background.update(0)
        elif player.sprite.health > 0 and score.sprite.score > 0:
            background.update(-9)
        menu.draw()
        if menu.options[0].active:
            pygame.time.set_timer(spawn_timer,0)
            game_active= True
            loading = True
            level = 1
            load_screen.sprite.prep(1)
            pygame.mouse.set_visible(False)
        if menu.options[1].active:
            pygame.quit()
            exit()
        
        end_screen.draw(screen)
        end_screen.update()
        game_over.draw(screen)
        game_over.update()

    if game_active and paused:
        background.draw(screen)
        spawners.draw(screen)
        goal.draw(screen)
        player_melee.draw(screen)
        player_projectiles.draw(screen)
        player.draw(screen)
        enemies.draw(screen)
        e_deco.draw(screen)
        platforms.draw(screen)
        foreground.draw(screen)
        screen.blit(test_top_dash,test_top_rect)
        score.draw(screen)
        hp_bar.draw()
        end_screen.draw(screen)
        screen.blit(pause_screen, pause_rect)


    #loading level 1
    if game_active and loading and level == 1:
        if load_screen.sprite.state == 0:
            background.draw(screen)
            menu.draw()
        else:
            background.draw(screen)
            spawners.draw(screen)
            player.draw(screen)
            enemies.draw(screen)
            e_deco.draw(screen)
            platforms.draw(screen)
            foreground.draw(screen)
            screen.blit(test_top_dash,test_top_rect)
            score.draw(screen)
            hp_bar.draw()
            e_death_animations.draw(screen)
            e_death_animations.update()
            e_projectiles.draw(screen)
            e_projectiles.update()

        load_screen.draw(screen)
        load_screen.update()
        if load_screen.sprite.load:
            load_level_1(player.sprite, player_projectiles, enemies, e_deco, e_death_animations, e_projectiles, platforms, spawners, screen_w, screen_h, background.sprite, foreground.sprite, goal)
            load_screen.sprite.load = False
            score.sprite.score = 0
        if not load_screen.sprite.active:
            loading = False
            pygame.time.set_timer(spawn_timer,5000)
    #loading level 2
    if game_active and loading and level == 2:
        background.draw(screen)
        spawners.draw(screen)
        player_melee.draw(screen)
        player_projectiles.draw(screen)
        player.draw(screen)
        enemies.draw(screen)
        e_deco.draw(screen)
        platforms.draw(screen)
        foreground.draw(screen)
        screen.blit(test_top_dash,test_top_rect)
        score.draw(screen)
        hp_bar.draw()
        e_death_animations.draw(screen)
        e_death_animations.update()
        e_projectiles.draw(screen)
        e_projectiles.update()

        load_screen.draw(screen)
        load_screen.update()
        if load_screen.sprite.load:
            load_level_2(player.sprite, player_projectiles, enemies, e_deco, e_death_animations, e_projectiles, platforms, spawners, screen_w, screen_h, background.sprite, foreground.sprite)
            load_screen.sprite.load = False
            player.sprite.attack = False
            player.sprite.attack_index = 0
            player_melee.update()   
        if not load_screen.sprite.active:
            loading = False
            pygame.time.set_timer(spawn_timer,4000)
    
    
    #loading level end
    if game_active and loading and level == -10:
        background.draw(screen)
        spawners.draw(screen)
        goal.draw(screen)
        player_melee.draw(screen)
        player_projectiles.draw(screen)
        player.draw(screen)
        enemies.draw(screen)
        e_deco.draw(screen)
        platforms.draw(screen)
        foreground.draw(screen)
        screen.blit(test_top_dash,test_top_rect)
        score.draw(screen)
        hp_bar.draw()
        e_death_animations.draw(screen)
        e_death_animations.update()
        e_projectiles.draw(screen)
        e_projectiles.update()

        load_screen.draw(screen)
        load_screen.update()
        if load_screen.sprite.load:
            load_level_end(player.sprite, player_projectiles, enemies, e_deco, e_death_animations, e_projectiles, platforms, spawners, screen_w, screen_h, background.sprite, foreground.sprite, goal)
            load_screen.sprite.load = False
            player.sprite.attack = False
            player.sprite.attack_index = 0
            player_melee.update()   
        if not load_screen.sprite.active:
            loading = False
            pygame.time.set_timer(spawn_timer,0)

    #active game
    if game_active and not loading and not paused:
        
    
        background.draw(screen)

        spawners.draw(screen)
        spawners.update()

        goal.draw(screen)

        player_melee.draw(screen)
        player_projectiles.draw(screen)
        player.draw(screen)
        player.update()
        if player.sprite.throw_projectile:
            player.sprite.throw_projectile = False
            player_projectiles.add(Player_projectile(player.sprite ))


        player_melee.update()
        player_projectiles.update()

        enemies.draw(screen)
        e_deco.draw(screen)
        enemies.update()
        e_projectiles.update()
        

        platforms.draw(screen)

        player_projectile_collision(enemies, player_projectiles, score.sprite)
        projectile_collision(platforms, player_projectiles)
        player_projectile_collision(e_projectiles, player_projectiles, score.sprite)
        projectile_collision(platforms, e_projectiles)
        player_melee_collision(player_melee.sprite, enemies, score.sprite)
        player_melee_collision(player_melee.sprite, e_projectiles, score.sprite)

        e_deco.update()

        e_death_animations.draw(screen)
        e_death_animations.update()

        e_projectiles.draw(screen)
        


        block_collision(player.sprite,platforms)
        for enemy in enemies:
            eblock_collision(enemy,platforms)

        player_take_melee(player.sprite, enemies)
        player_take_melee(player.sprite, e_projectiles)

        foreground.draw(screen)
        screen.blit(test_top_dash,test_top_rect)
        score.draw(screen)
        score.update()
        hp_bar.draw()

        if player.sprite.finish:
            game_over.sprite.active = True

            #game_active = False
        elif score.sprite.score >= 10 and level == 1:
            pygame.time.set_timer(spawn_timer,0)
            loading = True
            level = 2
            load_screen.sprite.prep(2)
        #end level check    
        elif score.sprite.score >= 30 and level == 2:
            pygame.time.set_timer(spawn_timer,0)
            loading = True
            level = -10
            load_screen.sprite.prep(-10)

        if pygame.sprite.spritecollide(player.sprite, goal, False):
            end_screen.sprite.active = True
            
        if end_screen.sprite.active:
            if level == -10:
                end_screen.draw(screen)
            end_screen.update()
        if end_screen.sprite.alpha >= 255:
            menu.text = 'The End!'
            menu.options[0].text = 'Play Again'
            game_active = False
        if game_over.sprite.active:
            if player.sprite.finish:
                game_over.draw(screen)
            game_over.update()
        if game_over.sprite.alpha >= 255:
            menu.text = 'Game Over'
            menu.options[0].text = 'Restart'
            background.update(0)
            game_active = False

    pygame.display.update()
    clock.tick(60)
    pass