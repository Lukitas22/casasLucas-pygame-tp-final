import pygame
from configs import Configs
from constants import *



class Loot():  
    def __init__(self, x, y, frame_rate_ms, scale = 1) -> None:
            self.idle = Configs.getSurfaceFromSpriteSheet(PATH_IMAGE + "\Loots\Cherries.png", 17, 1, scale = scale)
            self.collected = Configs.getSurfaceFromSpriteSheet(PATH_IMAGE + "\Loots\Collected.png", 6, 1, scale = scale)
            self.frame = 0
            self.animation = self.idle
            self.image = self.animation[self.frame]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.rect_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, self.rect.h)
            self.frame_rate_ms = frame_rate_ms
            self.elapsed_time_animation = 0


    def collect(self, main_player):
        if self.is_collected(main_player):
            print("entre")
            self.animation = self.collected
        
        self.frame = 0    
        #self.image = self.animation[self.frame]


    def is_collected(self, main_player):
        is_collected = False

        if self.rect_collition.colliderect(main_player.rect):
            print("toco")
            is_collected = True
            
        return is_collected


    def do_animation(self, delta_ms):
        self.elapsed_time_animation += delta_ms

        if self.elapsed_time_animation >= self.frame_rate_ms:
            self.elapsed_time_animation = 0

            if self.frame < len(self.animation) - 1:
                self.frame += 1
            else:
                self.frame = 0


    def update(self, delta_ms, main_player):
        self.collect(main_player)
        self.do_animation(delta_ms)


    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, RED, self.rect)
            pygame.draw.rect(screen, GREEN, self.rect_collition)
            
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)