import pygame
import sys
import json
from constants import *
from player import Player
from platforms import Platform
from enemy import Enemy
from decoration import Decoration
from loot import Loot
from control import Control
from traps import Trap


data = open("config.json")
json_config = json.load(data)

stage = json_config.get("stages").get("stage_1")

screen = pygame.display.set_mode((WIDTH_WINDOW, HEIGHT_WINDOW))
pygame.display.set_caption("Pixel Adventure")


pygame.init()

clock = pygame.time.Clock()
timer = int(pygame.time.get_ticks() + stage.get("scenario").get("initial_time") * 1000)

music = pygame.mixer.music.load(stage.get("scenario").get("music"))
music = pygame.mixer.music.play(-1)
music = pygame.mixer.music.set_volume(0.1)
background = pygame.image.load(stage.get("scenario").get("background"))
background = pygame.transform.scale(background, (WIDTH_WINDOW, HEIGHT_WINDOW))
borders_limits = Control()

traps_group = pygame.sprite.Group()

decoration_group = pygame.sprite.Group()

loot_group = pygame.sprite.Group()

enemy_group = pygame.sprite.Group()

platform_group = pygame.sprite.Group()


main_player = Player(stage.get("player"))

for index in range(stage.get("scenario").get("loot_count")):
    coords = stage.get("loots").get("loot_pos")[index]
    loot = Loot(coords.get("x"), coords.get("y"), loot_config=stage.get("loots"))
    loot_group.add(loot)


for index in range(stage.get("scenario").get("enemies_count")):
    coords = stage.get("enemies").get("enemy_pos")[index]
    enemy = Enemy(coords.get("x"), coords.get("y"), enemy_config=stage.get("enemies"))
    enemy_group.add(enemy)


for index in range(stage.get("scenario").get("platforms_count")):
    coords = stage.get("platforms").get("platforms_pos")[index]
    platform = Platform(coords.get("x"), coords.get("y"), platforms_config=stage.get("platforms"))
    platform_group.add(platform)


for index in range(stage.get("scenario").get("trap_count")):
    coords = stage.get("traps").get("traps_pos")[index]
    trap = Trap(coords.get("x"), coords.get("y"), trap_config=stage.get("traps"))
    traps_group.add(trap)



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
        enemy_element.update(delta_ms, platform_group, main_player)
        enemy_element.draw(screen)

    for platform in platform_group:
        platform.draw(screen)

    for trap in traps_group:
        trap.draw(screen)


    borders_limits.draw(screen)
    main_player.events(delta_ms, keys)
    main_player.update(delta_ms, platform_group, borders_limits, keys, enemy_group, traps_group)
    main_player.bullet_group.draw(screen)
    main_player.draw(screen)

    pygame.display.flip()
    
    


