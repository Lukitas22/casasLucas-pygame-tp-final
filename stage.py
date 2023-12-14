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



class Stage:
    def __init__(self, stage_config, screen) -> None:
        self.stage = stage_config
        self.screen = screen
        self.background = self.stage.get("backgound")
        self.background = pygame.transform.scale(self.background, (WIDTH_WINDOW, HEIGHT_WINDOW))
        self.clock = pygame.time.Clock()
        self.delta_ms = self.clock.tick(FPS)
        self.initial_time = self.stage.get("initial_time")
        self.timer = int(pygame.time.get_ticks() + self.initial_time * 1000)
        self.play = True

        self.borders_limits = Control()

        self.player = Player(self.stage.get("player"))
        
        self.enemy = pygame.sprite.Group()
        self.enemy_amount = self.stage.get("scenario").get("enemies_count")
        self.enemy_coords = list[dict] = self.stage.get("enemies").get("enemy_pos")

        self.traps = pygame.sprite.Group()
        self.trap_amount = self.stage.get("scenario").get("trap_count")
        self.trap_coords = list[dict] = self.stage.get("enemies").get("traps_pos")

        self.loot = pygame.sprite.Group()
        self.loot_amount = self.stage.get("scenario").get("loot_count")
        self.loot_coords = list[dict] = self.stage.get("enemies").get("loot_pos")

        self.platforms = pygame.sprite.Group()
        self.platform_amount= self.stage.get("scenario").get("platforms_count")
        self.platform_coords = list[dict] = self.stage.get("enemies").get("platforms_pos")


    # def set_render_fonts(self):
    #     font = pygame.font.SysFont("Arial", 26)
    #     self.text_timer = font.render("Tiempo Restante: {0}".format(self.time_remaining), True, WHITE)
    #     self.text_points = font.render("Puntos: {0}".format(self.player.score), True, WHITE)
    #     self.text_lives = font.render("Vidas: {0}".format(self.player.lives), True, WHITE)

    #     self.screen.blit(self.text_timer, (80, 10))
    #     self.screen.blit(self.text_points, (400, 10))
    #     self.screen.blit(self.text_lives, (600, 10))

    
    # def backgound_image(self):
    #     return self.background


    def add_enemy(self, enemy):
        self.enemy.add(enemy) 

    def add_loot(self, loot):
        self.loot.add(loot)

    def add_trap(self, trap):
        self.traps.add(trap)

    def add_platforms(self, platform):
        self.platforms.add(platform)


    def generate_enemies(self):
        if len(self.enemy) == 0:
            for index in range(self.enemy_amount):
                coords = self.enemy_coords[index]
                enemy = Enemy(coords.get("x"), coords.get("y"), self.stage.get("enemies"))
                self.add_anemy(enemy)

    def generate_traps(self):
        if len(self.traps) == 0:
            for index in range(self.trap_amount):
                coords = self.trap_coords[index]
                trap = Trap(coords.get("x"), coords.get("y"), self.stage.get("traps"))
                self.add_trap(trap)

    def generate_loots(self):
        if len(self.loot) == 0:
            for index in range(self.loot_amount):
                coords = self.loot_coords[index]
                loot = Loot(coords.get("x"), coords.get("y"), self.stage.get("loots"))
                self.add_loot(loot)

    def generate_platforms(self):
        if len(self.platforms) == 0:
            for index in range(self.platform_amount):
                coords = self.platform_coords[index]
                platform = Platform(coords.get("x"), coords.get("y"), self.stage.get("platforms"))
                self.add_platforms(platform)

















