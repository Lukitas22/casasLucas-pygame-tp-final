import pygame
import sys
from constants import *
from player import Player
from platforms import Platform
from enemy import Enemy
from decoration import Decoration
from loot import Loot

screen = pygame.display.set_mode((WIDTH_WINDOW, HEIGHT_WINDOW))

pygame.init()
clock = pygame.time.Clock()

background = pygame.image.load(PATH_IMAGE + "\Backgrounds\Green_2.png")
background = pygame.transform.scale(background, (WIDTH_WINDOW, HEIGHT_WINDOW))

decoration_group = pygame.sprite.Group()
decoration_grass_1 = Decoration("\Platform\grass.png", x = 0, y = 820)
decoration_grass_2 = Decoration("\Platform\grass.png", x = 48, y = 820)
decoration_grass_3 = Decoration("\Platform\grass.png", x = 96, y = 820)
decoration_grass_4 = Decoration("\Platform\grass.png", x = 144, y = 820)
decoration_grass_5 = Decoration("\Platform\grass.png", x = 192, y = 820)
decoration_grass_6 = Decoration("\Platform\grass.png", x = 240, y = 820)
decoration_grass_7 = Decoration("\Platform\grass.png", x = 288, y = 820)
decoration_grass_8 = Decoration("\Platform\grass.png", x = 336, y = 820)
decoration_grass_9 = Decoration("\Platform\grass.png", x = 384, y = 820)
decoration_grass_10 = Decoration("\Platform\grass.png", x = 432, y = 820)
decoration_grass_11 = Decoration("\Platform\grass.png", x = 480, y = 820)
decoration_grass_12 = Decoration("\Platform\grass.png", x = 528, y = 820)
decoration_grass_13 = Decoration("\Platform\grass.png", x = 576, y = 820)
decoration_grass_14 = Decoration("\Platform\grass.png", x = 624, y = 820)
decoration_grass_15 = Decoration("\Platform\grass.png", x = 672, y = 820)
decoration_grass_16 = Decoration("\Platform\grass.png", x = 720, y = 820)
decoration_grass_17 = Decoration("\Platform\grass.png", x = 768, y = 820)
decoration_grass_18 = Decoration("\Platform\grass.png", x = 816, y = 820)
decoration_grass_19 = Decoration("\Platform\grass.png", x = 864, y = 820)
decoration_grass_20 = Decoration("\Platform\grass.png", x = 912, y = 820)
decoration_grass_21 = Decoration("\Platform\grass.png", x = 960, y = 820)
decoration_grass_22 = Decoration("\Platform\grass.png", x = 1008, y = 820)
decoration_grass_23 = Decoration("\Platform\grass.png", x = 1056, y = 820)
decoration_grass_24 = Decoration("\Platform\grass.png", x = 1104, y = 820)
decoration_grass_25 = Decoration("\Platform\grass.png", x = 1152, y = 820)
decoration_grass_26 = Decoration("\Platform\grass.png", x = 1200, y = 820)
decoration_grass_27 = Decoration("\Platform\grass.png", x = 1248, y = 820)
decoration_grass_28 = Decoration("\Platform\grass.png", x = 1296, y = 820)
decoration_grass_29 = Decoration("\Platform\grass.png", x = 1344, y = 820)
decoration_grass_30 = Decoration("\Platform\grass.png", x = 1392, y = 820)
decoration_grass_31 = Decoration("\Platform\grass.png", x = 1440, y = 820)
decoration_black_1 = Decoration("\Platform\Black.png", x = 0, y = 868)
decoration_black_2 = Decoration("\Platform\Black.png", x = 48, y = 868)
decoration_black_3 = Decoration("\Platform\Black.png", x = 96, y = 868)
decoration_black_4 = Decoration("\Platform\Black.png", x = 144, y = 868)
decoration_black_5 = Decoration("\Platform\Black.png", x = 192, y = 868)
decoration_black_6 = Decoration("\Platform\Black.png", x = 240, y = 868)
decoration_black_7 = Decoration("\Platform\Black.png", x = 288, y = 868)
decoration_black_8 = Decoration("\Platform\Black.png", x = 336, y = 868)
decoration_black_9 = Decoration("\Platform\Black.png", x = 384, y = 868)
decoration_black_10 = Decoration("\Platform\Black.png", x = 432, y = 868)
decoration_black_11 = Decoration("\Platform\Black.png", x = 480, y = 868)
decoration_black_12 = Decoration("\Platform\Black.png", x = 528, y = 868)
decoration_black_13 = Decoration("\Platform\Black.png", x = 576, y = 868)
decoration_black_14 = Decoration("\Platform\Black.png", x = 624, y = 868)
decoration_black_15 = Decoration("\Platform\Black.png", x = 672, y = 868)
decoration_black_16 = Decoration("\Platform\Black.png", x = 720, y = 868)
decoration_black_17 = Decoration("\Platform\Black.png", x = 768, y = 868)
decoration_black_18 = Decoration("\Platform\Black.png", x = 816, y = 868)
decoration_black_19 = Decoration("\Platform\Black.png", x = 864, y = 868)
decoration_black_20 = Decoration("\Platform\Black.png", x = 912, y = 868)
decoration_black_21 = Decoration("\Platform\Black.png", x = 960, y = 868)
decoration_black_22 = Decoration("\Platform\Black.png", x = 1008, y = 868)
decoration_black_23 = Decoration("\Platform\Black.png", x = 1056, y = 868)
decoration_black_24 = Decoration("\Platform\Black.png", x = 1104, y = 868)
decoration_black_25 = Decoration("\Platform\Black.png", x = 1152, y = 868)
decoration_black_26 = Decoration("\Platform\Black.png", x = 1200, y = 868)
decoration_black_27 = Decoration("\Platform\Black.png", x = 1248, y = 868)
decoration_black_28 = Decoration("\Platform\Black.png", x = 1296, y = 868)
decoration_black_29 = Decoration("\Platform\Black.png", x = 1344, y = 868)
decoration_black_30 = Decoration("\Platform\Black.png", x = 1392, y = 868)
decoration_black_31 = Decoration("\Platform\Black.png", x = 1440, y = 868)
decoration_black_32 = Decoration("\Platform\Black.png", x = 1488, y = 868)


decoration_group.add(decoration_grass_1)
decoration_group.add(decoration_grass_2)
decoration_group.add(decoration_grass_3)
decoration_group.add(decoration_grass_4)
decoration_group.add(decoration_grass_5)
decoration_group.add(decoration_grass_6)
decoration_group.add(decoration_grass_7)
decoration_group.add(decoration_grass_8)
decoration_group.add(decoration_grass_9)
decoration_group.add(decoration_grass_10)
decoration_group.add(decoration_grass_11)
decoration_group.add(decoration_grass_12)
decoration_group.add(decoration_grass_13)
decoration_group.add(decoration_grass_14)
decoration_group.add(decoration_grass_15)
decoration_group.add(decoration_grass_16)
decoration_group.add(decoration_grass_17)
decoration_group.add(decoration_grass_18)
decoration_group.add(decoration_grass_19)
decoration_group.add(decoration_grass_20)
decoration_group.add(decoration_grass_21)
decoration_group.add(decoration_grass_22)
decoration_group.add(decoration_grass_23)
decoration_group.add(decoration_grass_24)
decoration_group.add(decoration_grass_25)
decoration_group.add(decoration_grass_26)
decoration_group.add(decoration_grass_27)
decoration_group.add(decoration_grass_28)
decoration_group.add(decoration_grass_29)
decoration_group.add(decoration_grass_30)
decoration_group.add(decoration_grass_31)
decoration_group.add(decoration_black_1)
decoration_group.add(decoration_black_2)
decoration_group.add(decoration_black_3)
decoration_group.add(decoration_black_4)
decoration_group.add(decoration_black_5)
decoration_group.add(decoration_black_6)
decoration_group.add(decoration_black_7)
decoration_group.add(decoration_black_8)
decoration_group.add(decoration_black_9)
decoration_group.add(decoration_black_10)
decoration_group.add(decoration_black_11)
decoration_group.add(decoration_black_12)
decoration_group.add(decoration_black_13)
decoration_group.add(decoration_black_14)
decoration_group.add(decoration_black_15)
decoration_group.add(decoration_black_16)
decoration_group.add(decoration_black_17)
decoration_group.add(decoration_black_18)
decoration_group.add(decoration_black_19)
decoration_group.add(decoration_black_20)
decoration_group.add(decoration_black_21)
decoration_group.add(decoration_black_22)
decoration_group.add(decoration_black_23)
decoration_group.add(decoration_black_24)
decoration_group.add(decoration_black_25)
decoration_group.add(decoration_black_26)
decoration_group.add(decoration_black_27)
decoration_group.add(decoration_black_28)
decoration_group.add(decoration_black_29)
decoration_group.add(decoration_black_30)
decoration_group.add(decoration_black_31)
decoration_group.add(decoration_black_32)


main_player = Player(x = 0, y = 700, speed = 10, gravity = 20, jump_power = 20, frame_rate_ms = 55, move_frame_rate_ms = 40, jump_height = 150, scale = 2, interval_time_jump = 300)

enemy_list = []
enemy_list.append (Enemy(x=450,y=400,speed=6,gravity=14,jump_power=30,frame_rate_ms=150,move_frame_rate_ms=50,jump_height=140,scale= 2,interval_time_jump=300))
enemy_list.append (Enemy(x=750,y=400,speed=6,gravity=14,jump_power=30,frame_rate_ms=150,move_frame_rate_ms=50,jump_height=140,scale=2,interval_time_jump=300))


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
        enemy_element.update(delta_ms, list_platforms)
        enemy_element.draw(screen)

    for platform in list_platforms:
        platform.draw(screen)

    loot.update(delta_ms, main_player)
    loot.draw(screen)
    main_player.events(delta_ms, keys)
    main_player.update(delta_ms, list_platforms)
    main_player.draw(screen)

    pygame.display.flip()
    
    


