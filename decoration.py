import pygame
from constants import *



class Decoration(pygame.sprite.Sprite):
    def __init__(self, path, x, y):
        super().__init__()
        self.image = pygame.image.load(PATH_IMAGE + path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def draw(self, screen):
        screen.blit(self.image, self.rect)
