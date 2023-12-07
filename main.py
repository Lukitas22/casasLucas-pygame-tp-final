import pygame
import sys
from constants import *
from player import Player
from platforms import Platform
from enemy import Enemy
from decoration import Decoration
from loot import Loot
from control import Control

screen = pygame.display.set_mode((WIDTH_WINDOW, HEIGHT_WINDOW))

pygame.init()
clock = pygame.time.Clock()

background = pygame.image.load(PATH_IMAGE + "\Backgrounds\Primer_nivel.png")
background = pygame.transform.scale(background, (WIDTH_WINDOW, HEIGHT_WINDOW))
borders_limits = Control()

decoration_group = pygame.sprite.Group()


main_player = Player(x = 100, y = 700, speed = 10, gravity = 20, jump_power = 20, frame_rate_ms = 55, move_frame_rate_ms = 40, jump_height = 150, scale = 2, interval_time_jump = 300)

enemy_list = []
enemy_list.append (Enemy(x=450,y=700,speed=6,gravity=14,jump_power=30,frame_rate_ms=150,move_frame_rate_ms=50,jump_height=140,scale= 2,interval_time_jump=300))
enemy_list.append (Enemy(x=750,y=700,speed=6,gravity=14,jump_power=30,frame_rate_ms=150,move_frame_rate_ms=50,jump_height=140,scale=2,interval_time_jump=300))


list_platforms = []
list_platforms.append(Platform(x = 650, y = 700, width = 50, height = 50, type = 2))
list_platforms.append(Platform(x = 700, y = 700, width = 50, height = 50, type = 2))
list_platforms.append(Platform(x = 750, y = 700, width = 50, height = 50, type = 2))



loot = Loot(x = 100, y = 700, frame_rate_ms = 45, scale = 1.50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed() 

    delta_ms = clock.tick(FPS) 
    screen.blit(background, background.get_rect())
    
    for decoration in decoration_group:
        decoration.draw(screen)

    for enemy_element in enemy_list:
        enemy_element.update(delta_ms, list_platforms, main_player)
        enemy_element.draw(screen)

    for platform in list_platforms:
        platform.draw(screen)

    borders_limits.draw(screen)
    loot.update(delta_ms, main_player)
    loot.draw(screen)
    main_player.events(delta_ms, keys)
    main_player.update(delta_ms, list_platforms)
    main_player.draw(screen)

    pygame.display.flip()
    
    


