import pygame
from constants import *
from gui_widget import Widget
from gui_button import Button


class Form(Widget):
    def __init__(self, surface, x, y, widht, height, background_color, border_color, active) -> None:
        super().__init__(surface, x, y, widht, height, background_color, border_color)
        self.slave_surface = pygame.Surface((widht, height))
        self.slave_surface_rect = self.slave_surface.get_rect()
        self.slave_surface_rect.x = x
        self.slave_surface_rect.y = y
        self.active = active
    
    def render(self):
        pass


    def update(self, events):
        pass


class FormMenu(Form):
    def __init__(self, surface, x, y, widht, height, background_color, border_color, active):
        super().__init__(surface, x, y, widht, height, background_color, border_color, active)
        self.button_1 = Button(self.slave_surface, x = 100, y = 50, widht = 200, height = 50, background_color = WHITE, border_color = BLUE, on_click = self.on_click_button_1, on_click_param = "1234", text = "MENU", font="Arial", font_size=30, font_color=RED)
        self.button_2 = Button(self.slave_surface, x = 200, y = 50, widht = 200, height = 50, background_color = WHITE, border_color = BLUE, on_click = self.on_click_button_1, on_click_param = "8", text = "SETTINGS", font="Arial", font_size=30, font_color=RED)   
        self.button_list = [self.button_1, self.button_2]



    def on_click_button_1(parametro):
            print("CLICK", parametro)


    def update(self, events):
        for button in self.button_list:
            button.update(events)

    def draw(self):
        super().draw()

        for button in self.button_list:
            button.draw()
    










