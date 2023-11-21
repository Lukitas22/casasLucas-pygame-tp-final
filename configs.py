import pygame
from constants import *

class Configs:
    @staticmethod
    def getSurfaceFromSpriteSheet(path, columns, rows, flip = False, scale = 1):
        list_frames = []
        surface_image = pygame.image.load(path)
        width_frame = int(surface_image.get_width()/columns)
        height_frame = int(surface_image.get_height()/rows)
        width_frame_scaled = int(width_frame * scale)
        height_frame_scaled = int(height_frame * scale)

        for row in range(rows):
            for column in range(columns):
                x = column * width_frame
                y = row * height_frame
                surface_frame = surface_image.subsurface(x, y, width_frame, height_frame)
                if scale != 1:
                    surface_frame = pygame.transform.scale(surface_frame, (width_frame_scaled, height_frame_scaled)).convert_alpha()
                if flip:
                    surface_frame = pygame.transform.flip(surface_frame, True, False)
                list_frames.append(surface_frame)

        return list_frames


    @staticmethod
    def getSurfaceFromSeparateFiles(path_format, from_index, quantity, flip = False, scale = 1, w = 0, h = 0, repeat_frame = 1):
        list = []

        for i in range(from_index, quantity + from_index):
            path = path_format.format(i)
            surface_frame = pygame.image.load(path)
            width_frame_scaled = int(surface_frame.get_rect().w * scale)
            height_frame_scaled = int(surface_frame.get_rect().h * scale)
            if(scale == 1 and w != 0 and h != 0):
                surface_frame = pygame.transform.scale(surface_frame, (w, h)).convert_alpha()
            if(scale != 1):
                surface_frame = pygame.transform.scale(surface_frame, (width_frame_scaled, height_frame_scaled)).convert_alpha() 
            if(flip):
                surface_frame = pygame.transform.flip(surface_frame, True, False).convert_alpha() 
            
            for i in range(repeat_frame):
                list.append(surface_frame)
                
        return list
    


# def rescale_images(list_images, size):
#     for i in range(len(list_images)):
#         list_images[i] = pygame.transform.scale(list_images[i], size)
        

# def flip_images(list_original, flip_x, flip_y):
#     flipped_list = []

#     for image in list_original:
#         flipped_list.append(pygame.transform.flip(image, flip_x, flip_y))

#     return flipped_list

# def obtain_rects(principal):
#     dict = {}
#     dict["main"] = principal
#     dict["bottom"] = pygame.Rect(principal.left, principal.bottom - 6, principal.widht, 6)
#     dict["right"] = pygame.Rect(principal.right - 2, principal.top, 2, principal.height)
#     dict["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
#     dict["top"] = pygame.Rect(principal.left, principal.top, principal.widht, 6)
    
#     return dict


# player_idle = getSurfaceFromSpriteSheet(PATH_IMAGE + "\Main_Character\FrogNinja\Idle.png", 11, 1)

# player_walk = getSurfaceFromSpriteSheet(PATH_IMAGE + "\Main_Character\FrogNinja\Run.png", 12, 1)

# player_walk_left = flip_images(player_walk, True, False)


