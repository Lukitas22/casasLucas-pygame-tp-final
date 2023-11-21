import pygame
from constants import *
from configs import *


class Platform:
    def __init__(self, x, y, width, height, type = 0) -> None:
        self.image_list = Configs.getSurfaceFromSeparateFiles(PATH_IMAGE + "\Platform\{0}.png", 1, 25, w = width, h = height)

        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_RECT_H)


    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, RED, self.rect)

        screen.blit(self.image, self.rect)

        if DEBUG:
            pygame.draw.rect(screen, GREEN, self.rect_ground_collition)
    










