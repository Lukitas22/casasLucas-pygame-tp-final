import pygame
import sys
from constants import *
from gui_form import FormMenu


screen = pygame.display.set_mode((WIDTH_WINDOW, HEIGHT_WINDOW))
pygame.display.set_caption("Pixel Adventure")
pygame.init()

clock = pygame.time.Clock()


form_menu = FormMenu(surface= screen, x = 0, y = 0, widht = 100, height = 800, background_color = WHITE, border_color = BLUE, active = True)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed() 
    delta_ms = clock.tick(FPS) 


    if(form_menu.active):
        form_menu.update(events)
        form_menu.draw()

    pygame.display.flip()
    
    


