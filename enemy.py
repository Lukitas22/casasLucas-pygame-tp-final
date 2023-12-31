import pygame
from constants import *
from configs import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy_config) -> None:
        super().__init__()
        self.enemy_config = enemy_config
        self.walk_l = Configs.getSurfaceFromSpriteSheet(self.enemy_config.get("sprites").get("walk"), 14, 1, scale = self.enemy_config.get("scale"))
        self.walk_r = Configs.getSurfaceFromSpriteSheet(self.enemy_config.get("sprites").get("walk"), 14, 1, flip = True, scale = self.enemy_config.get("scale"))
        self.idle_l = Configs.getSurfaceFromSpriteSheet(self.enemy_config.get("sprites").get("idle"), 13, 1, scale = self.enemy_config.get("scale"))
        self.idle_r = Configs.getSurfaceFromSpriteSheet(self.enemy_config.get("sprites").get("idle"), 13, 1, flip = True, scale = self.enemy_config.get("scale"))
    
        self.contador = 0
        self.move_x = 0
        self.move_y = 0
        self.speed = self.enemy_config.get("speed")
        self.gravity = self.enemy_config.get("gravity")
        self.jump_power = self.enemy_config.get("jump_power")
        self.is_jump = False
        self.y_start_jump = 0
        self.jump_height = self.enemy_config.get("jump_height")
        self.elapsed_time_jump = 0
        self.time_last_jump = 0
        self.interval_time_jump = self.enemy_config.get("interval_time_jump")
        self.is_fall = False
        self.elapsed_time_move = 0
        self.elapsed_time_animation = 0
        self.move_frame_rate_ms = self.enemy_config.get("move_frame_rate_ms")
        self.frame_rate_ms = self.enemy_config.get("frame_rate_ms")
        self.frame = 0
        self.animation = self.idle_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w / 4, self.rect.y + self.rect.h - GROUND_RECT_H, self.rect.w / 2, GROUND_RECT_H)
        self.rect_head_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_RECT_H)
        self.rect_left_collition = pygame.Rect(self.rect.x, self.rect.y + self.rect.w / 4, self.rect.w / 6, self.rect.h / 2)
        self.rect_right_collition = pygame.Rect(self.rect.x + self.rect.w - 10, self.rect.y + self.rect.w / 4, self.rect.w / 6, self.rect.h / 2)


    def change_x(self, delta_x):
        self.rect.x += delta_x
        self.rect_ground_collition.x += delta_x
        self.rect_head_collition.x += delta_x
        self.rect_left_collition.x += delta_x
        self.rect_right_collition.x += delta_x


    def change_y(self, delta_y):
        self.rect.y += delta_y
        self.rect_ground_collition.y += delta_y
        self.rect_head_collition.y += delta_y
        self.rect_left_collition.y += delta_y
        self.rect_right_collition.y += delta_y


    def do_movement(self, delta_ms, list_platforms):
        self.elapsed_time_move += delta_ms

        if self.elapsed_time_move >= self.move_frame_rate_ms:
            self.elapsed_time_move = 0

            if not self.is_on_platform(list_platforms):
                if self.move_y == 0:
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                self.is_fall = False
                self.change_x(self.move_x)
                if self.contador <= 50:
                    self.move_x = -self.speed
                    self.animation = self.walk_l
                    self.contador += 1 
                elif self.contador <= 100:
                    self.move_x = self.speed
                    self.animation = self.walk_r
                    self.contador += 1
                else:
                    self.contador = 0


    def is_on_platform(self, list_platforms):
        is_on_platform = False

        if self.rect.y >= GROUND_LEVEL:
            is_on_platform = True
        else:
            for platform in list_platforms:
                if self.rect_ground_collition.colliderect(platform.rect_ground_collition):
                    is_on_platform = True
                    break

        return is_on_platform
    

    def dead(self, main_player):
        if self.is_dead(main_player):
            main_player.score += 100
            print("entre")
            self.kill()


    def is_dead(self, main_player):
        is_dead = False
        if self.rect_head_collition.colliderect(main_player.rect_ground_collition):
            is_dead = True
            print("muere")

        return is_dead
    
    
    def do_animation(self, delta_ms):
        self.elapsed_time_animation += delta_ms

        if self.elapsed_time_animation >= self.frame_rate_ms:
            self.elapsed_time_animation = 0

            if self.frame < len(self.animation) - 1:
                self.frame += 1
            else:
                self.frame = 0


    def update(self, delta_ms, list_platforms, main_player):
        self.dead(main_player)
        self.do_movement(delta_ms, list_platforms)
        self.do_animation(delta_ms)


    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, RED, self.rect)
            pygame.draw.rect(screen, GREEN, self.rect_ground_collition)
            pygame.draw.rect(screen, GREEN, self.rect_head_collition)
            pygame.draw.rect(screen, BLUE, self.rect_left_collition)
            pygame.draw.rect(screen, BLUE, self.rect_right_collition)
            
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)
