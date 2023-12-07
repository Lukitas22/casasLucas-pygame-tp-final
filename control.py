import pygame
from constants import *


class Control:
    def __init__(self) -> None:
        self.rect_right_border = pygame.Rect(1436, 10, 10, 900)
        self.rect_left_border = pygame.Rect(55, 10, 10, 900)
        self.rect_top_border = pygame.Rect(40, 49, 1500, 10)


    def collition(self, main_player):
        pass


    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, BLUE, self.rect_right_border)
            pygame.draw.rect(screen, BLUE, self.rect_left_border)
            pygame.draw.rect(screen, BLUE, self.rect_top_border)
            