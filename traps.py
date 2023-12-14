import pygame
from configs import Configs
from constants import *


class Trap(pygame.sprite.Sprite):
    def __init__(self, x, y, trap_config) -> None:
        super().__init__()
        self.trap_config = trap_config
        self.image = pygame.image.load(self.trap_config.get("sprite"))
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, RED, self.rect)

        screen.blit(self.image, self.rect)



