import pygame
import sys
from constants import *
from player import Player
from platforms import Platform
from enemy import Enemy
from decoration import Decoration
from loot import Loot
from control import Control
from traps import Trap


screen = pygame.display.set_mode((WIDTH_WINDOW, HEIGHT_WINDOW))
pygame.display.set_caption("Pixel Adventure")

pygame.init()

initial_time = 60 
clock = pygame.time.Clock()
timer = int(pygame.time.get_ticks() + initial_time * 1000)

background = pygame.image.load(PATH_IMAGE + "\Backgrounds\Primer_nivel.png")
background = pygame.transform.scale(background, (WIDTH_WINDOW, HEIGHT_WINDOW))
borders_limits = Control()

traps_group= pygame.sprite.Group()

decoration_group = pygame.sprite.Group()

loot_group = pygame.sprite.Group()

enemy_group = pygame.sprite.Group()

loot_1 = Loot(x = 225, y = 650, frame_rate_ms = 45, scale = 1.50)
loot_2 = Loot(x = 375, y = 550, frame_rate_ms = 45, scale = 1.50)
loot_3 = Loot(x = 600, y = 400, frame_rate_ms = 45, scale = 1.50)
loot_4 = Loot(x = 875, y = 300, frame_rate_ms = 45, scale = 1.50)
loot_5 = Loot(x = 1150, y = 100, frame_rate_ms = 45, scale = 1.50)

loot_group.add(loot_1)
loot_group.add(loot_2)
loot_group.add(loot_3)
loot_group.add(loot_4)
loot_group.add(loot_5)


main_player = Player(x = 100, y = 700, speed = 10, gravity = 20, jump_power = 20, frame_rate_ms = 55, move_frame_rate_ms = 40, jump_height = 150, scale = 2, interval_time_jump = 300)


enemy_1 = Enemy(x=1300,y=100,speed=6,gravity=14,jump_power=30,frame_rate_ms=150,move_frame_rate_ms=50,jump_height=140,scale= 2,interval_time_jump=300)
enemy_2 = Enemy(x=750,y=400,speed=6,gravity=14,jump_power=30,frame_rate_ms=150,move_frame_rate_ms=50,jump_height=140,scale=2,interval_time_jump=300)

enemy_group.add(enemy_1)
enemy_group.add(enemy_2)


list_platforms = []

list_platforms.append(Platform(x = 200, y = 700, width = 50, height = 50, type = 2))
list_platforms.append(Platform(x = 250, y = 700, width = 50, height = 50, type = 2))

list_platforms.append(Platform(x = 350, y = 600, width = 50, height = 50, type = 2))
list_platforms.append(Platform(x = 400, y = 600, width = 50, height = 50, type = 2))

list_platforms.append(Platform(x = 450, y = 500, width = 50, height = 50, type = 2))
list_platforms.append(Platform(x = 500, y = 500, width = 50, height = 50, type = 2))
list_platforms.append(Platform(x = 550, y = 500, width = 50, height = 50, type = 2))
list_platforms.append(Platform(x = 600, y = 500, width = 50, height = 50, type = 2))
list_platforms.append(Platform(x = 650, y = 500, width = 50, height = 50, type = 2))
list_platforms.append(Platform(x = 700, y = 500, width = 50, height = 50, type = 2))
list_platforms.append(Platform(x = 750, y = 500, width = 50, height = 50, type = 2))

list_platforms.append(Platform(x = 850, y = 350, width = 50, height = 50, type = 2))
list_platforms.append(Platform(x = 900, y = 350, width = 50, height = 50, type = 2))

list_platforms.append(Platform(x = 1000, y = 200, width = 50, height = 50, type = 2))
list_platforms.append(Platform(x = 1050, y = 200, width = 50, height = 50, type = 2))
list_platforms.append(Platform(x = 1100, y = 200, width = 50, height = 50, type = 2))
list_platforms.append(Platform(x = 1150, y = 200, width = 50, height = 50, type = 2))
list_platforms.append(Platform(x = 1200, y = 200, width = 50, height = 50, type = 2))
list_platforms.append(Platform(x = 1250, y = 200, width = 50, height = 50, type = 2))
list_platforms.append(Platform(x = 1300, y = 200, width = 50, height = 50, type = 2))


trap_1 = Trap(x = 510, y = 475)
trap_2 = Trap(x = 710, y = 475)
trap_3 = Trap(x = 1060, y = 175)
trap_4 = Trap(x = 1260, y = 175)

traps_group.add(trap_1)
traps_group.add(trap_2)
traps_group.add(trap_3)
traps_group.add(trap_4)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed() 

    time_remaining = max(0, (timer - pygame.time.get_ticks()) // 1000)

    font = pygame.font.SysFont("Arial", 26)
    text_timer = font.render("Tiempo Restante: {0}".format(time_remaining), True, WHITE)
    text_points = font.render("Puntos: {0}".format(main_player.score), True, WHITE)
    text_lives = font.render("Vidas: {0}".format(main_player.lives), True, WHITE)

    if time_remaining == 0:
        print("You lose")
        break
    

    delta_ms = clock.tick(FPS) 
    screen.blit(background, background.get_rect())
    screen.blit(text_timer, (80, 10))
    screen.blit(text_points, (400, 10))
    screen.blit(text_lives, (600, 10))
   
    for loot in loot_group:
        loot.update(delta_ms, main_player)
        loot.draw(screen)
    
    for decoration in decoration_group:
        decoration.draw(screen)

    for enemy_element in enemy_group:
        enemy_element.update(delta_ms, list_platforms, main_player)
        enemy_element.draw(screen)

    for platform in list_platforms:
        platform.draw(screen)

    for trap in traps_group:
        trap.draw(screen)

    borders_limits.draw(screen)
    main_player.events(delta_ms, keys)
    main_player.update(delta_ms, list_platforms, borders_limits, keys, enemy_element, trap)
    main_player.bullet_group.draw(screen)
    main_player.draw(screen)

    pygame.display.flip()
    
    


