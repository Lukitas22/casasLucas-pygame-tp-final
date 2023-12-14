import pygame
from constants import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, speed, direction):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=pos)
        self.direction = direction
        self.speed = speed


    def destroy(self, enemy, borders_limits):
        if self.rect.x >= WIDTH_WINDOW or self.rect.x <= 0 or self.rect.colliderect(borders_limits.rect_right_border) or self.rect.colliderect(borders_limits.rect_left_border):
            self.kill()
        if self.rect.colliderect(enemy.rect):
            self.kill()
            enemy.kill()

            


    def update(self, enemy_group, borders_limits):
        if self.direction == DIRECTION_R:
            self.rect.x -= self.speed
            self.destroy(enemy_group, borders_limits)

        elif self.direction == DIRECTION_L:
            self.rect.x += self.speed
            self.destroy(enemy_group, borders_limits)
            





































