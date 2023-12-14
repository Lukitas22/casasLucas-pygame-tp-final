import pygame
from configs import Configs
from constants import *


class Trap:
    def __init__(self, x, y) -> None:
        self.image = pygame.image.load(PATH_IMAGE +  "\Traps\Idle.png")
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, RED, self.rect)

        screen.blit(self.image, self.rect)



