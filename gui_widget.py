import pygame
from constants import *



class Widget:
    def __init__(self, surface, x, y, widht, height, background_color, border_color) -> None:
        self.surface = surface
        self.x = x
        self.y = y
        self.w = widht
        self.h = height
        self.background_colour = background_color
        self.border_colour = border_color

    def render(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.surface.blit(self.slave_surface, self.slave_surface_rect)

