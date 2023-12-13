import pygame
from constants import *
from gui_widget import Widget


class Button(Widget):
    def __init__(self, surface, x, y, widht, height, background_color, border_color, on_click, on_click_param, text, font, font_size, font_color) -> None:
        super().__init__(surface, x, y, widht, height, background_color, border_color)
        pygame.font.init()

        self.on_click = on_click
        self.on_click_param = on_click_param
        self._text = text
        self.font = pygame.font.SysFont(font, font_size) 
        self.font_color = font_color

    
    def render(self):
        image_text = self.font.render(self._text, True, self.font_color, self.background_colour)
        self.slave_surface = pygame.surface.Surface((self.w, self.h))
        self.slave_surface_rect = self.slave_surface.get_rect()
        #self.slave_surface_rect_collide = 
        self.slave_surface_rect.x = self.x
        self.slave_surface_rect.y = self.y
        

        self.slave_surface.fill(self.background_colour)
        
        self.slave_surface.blit(image_text,(5,5))


    def update(self, events):

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.slave_surface_rect.collidepoint(event.pos):
                    self.on_click(self.on_click_param)

        self.render()

    