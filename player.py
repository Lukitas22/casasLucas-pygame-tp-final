import pygame
from constants import *
from configs import *
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, player_config) -> None:
        super().__init__()
        self.player_config = player_config
        self.walk_r = Configs.getSurfaceFromSpriteSheet(self.player_config.get("sprites").get("walk"), 12, 1, scale = self.player_config.get("scale"))
        self.walk_l = Configs.getSurfaceFromSpriteSheet(self.player_config.get("sprites").get("walk"), 12, 1, flip = True, scale = self.player_config.get("scale"))
        self.jump_r = Configs.getSurfaceFromSpriteSheet(self.player_config.get("sprites").get("jump"), 1, 1, scale = self.player_config.get("scale"))
        self.jump_l = Configs.getSurfaceFromSpriteSheet(self.player_config.get("sprites").get("jump"), 1, 1, flip = True, scale = self.player_config.get("scale"))
        self.idle_r = Configs.getSurfaceFromSpriteSheet(self.player_config.get("sprites").get("idle"), 11, 1, scale = self.player_config.get("scale"))
        self.idle_l = Configs.getSurfaceFromSpriteSheet(self.player_config.get("sprites").get("idle"), 11, 1, flip = True, scale = self.player_config.get("scale"))
        self.bullet_group = pygame.sprite.Group()
        self.bullet_cooldown = 600
        self.bullet_time = 0
        self.sound_shoot = pygame.mixer.Sound(PATH_SOUND_SHOOT)
        self.ready = True
        self.lives = self.player_config.get("lives")
        self.score = 0
        self.direction = DIRECTION_R 
        self.move_x = 0
        self.move_y = 0
        self.speed_to_change = self.player_config.get("speed")
        self.speed = self.player_config.get("speed")
        self.gravity = self.player_config.get("gravity")
        self.jump_power = self.player_config.get("jump_power")
        self.is_jump = False
        self.y_start_jump = 0
        self.jump_height = self.player_config.get("jump_height")
        self.elapsed_time_jump = 0
        self.time_last_jump = 0
        self.interval_time_jump = self.player_config.get("interval_time_jump")
        self.is_fall = False
        self.elapsed_time_move = 0
        self.elapsed_time_animation = 0
        self.move_frame_rate_ms = self.player_config.get("move_frame_rate_ms")
        self.frame_rate_ms = self.player_config.get("frame_rate_ms")
        self.frame = 0
        self.animation = self.idle_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = self.player_config.get("x")
        self.rect.y = self.player_config.get("y")
        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w / 4, self.rect.y + self.rect.h - GROUND_RECT_H, self.rect.w / 2, GROUND_RECT_H)
        self.rect_head_collition = pygame.Rect(self.rect.x + self.rect.w / 4, self.rect.y, self.rect.w / 2, GROUND_RECT_H)


    def walk(self, direction):
        if self.is_jump == False and self.is_fall == False:
            if self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l):
                self.frame = 0
                self.direction = direction
                
            if direction == DIRECTION_R:
                self.move_x = self.speed_to_change
                self.animation = self.walk_r
            else:
                self.move_x = -self.speed_to_change
                self.animation = self.walk_l


    def jump(self, on_off = True):
        if on_off and self.is_jump == False and self.is_fall == False:
            self.y_start_jump = self.rect.y

            if self.direction == DIRECTION_R:
                self.move_x = int(self.move_x / 1)
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = int(self.move_x / 1)
                self.move_y = -self.jump_power
                self.animation = self.jump_l

            self.frame = 0    
            self.is_jump = True

        if on_off == False:
            self.is_jump = False
            self.idle()


    def idle(self):
        if self.animation != self.idle_l and self.animation != self.idle_r:
            if self.direction == DIRECTION_R:
                self.animation = self.idle_r
            else:
                self.animation = self.idle_l
                
            self.move_x = 0
            self.move_y = 0
            self.frame = 0  


    def dead(self, enemy_group, traps_group):
        for trap in traps_group:
            if self.rect.colliderect(trap.rect):
                self.lives -= 1
            if self.lives == 0:
                print("Mori")

        for enemy in enemy_group:   
            if self.rect.colliderect(enemy.rect_left_collition) or self.rect.colliderect(enemy.rect_right_collition) or self.rect.colliderect(trap.rect):
                self.lives -= 1
            if self.lives == 0:
                print("Mori")


    def shoot(self):
        self.bullet_group.add(Bullet(self.rect.center, -8, self.direction))
        self.sound_shoot.play().set_volume(0.2)

    
    def recharge(self):
        if not self.ready:
            curent_time = pygame.time.get_ticks()
            if curent_time - self.bullet_time >= self.bullet_cooldown:
                self.ready = True


    def collition_borders(self, borders, keys):
        if self.rect.colliderect(borders.rect_right_border):
            self.speed_to_change = 0
            if keys[pygame.K_LEFT]:
                self.speed_to_change = self.speed

        if self.rect.colliderect(borders.rect_left_border): 
            self.speed_to_change = 0
            if keys[pygame.K_RIGHT]:
                self.speed_to_change = self.speed
        
        if self.rect.colliderect(borders.rect_top_border):
            self.jump(False)


    def change_x(self, delta_x):
        self.rect.x += delta_x
        self.rect_ground_collition.x += delta_x
        self.rect_head_collition.x += delta_x


    def change_y(self, delta_y):
        self.rect.y += delta_y
        self.rect_ground_collition.y += delta_y
        self.rect_head_collition.y += delta_y


    def do_movement(self, delta_ms, list_platforms):
        self.elapsed_time_move += delta_ms

        if self.elapsed_time_move >= self.move_frame_rate_ms:
            self.elapsed_time_move = 0

            if abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump:
                self.move_y = 0

            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if not self.is_on_platform(list_platforms):
                if self.move_y == 0:
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if self.is_jump:
                    self.jump(False)
                self.is_fall = False


    def is_on_platform(self, list_platforms):
        is_on_platform = False

        if self.rect.y >= GROUND_LEVEL:
            is_on_platform = True
        else:
            for platform in list_platforms:
                if self.rect_ground_collition.colliderect(platform.rect_ground_collition):
                    is_on_platform = True
                    break

        return is_on_platform


    def do_animation(self, delta_ms):
        self.elapsed_time_animation += delta_ms

        if self.elapsed_time_animation >= self.frame_rate_ms:
            self.elapsed_time_animation = 0

            if self.frame < len(self.animation) - 1:
                self.frame += 1
            else:
                self.frame = 0


    def update(self, delta_ms, list_platforms, borders, keys, enemy_group, traps_group):
        self.dead(enemy_group, traps_group)
        self.recharge()
        self.bullet_group.update(enemy_group, borders)
        self.collition_borders(borders, keys)
        self.do_movement(delta_ms, list_platforms)
        self.do_animation(delta_ms)
        

    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, RED, self.rect)
            pygame.draw.rect(screen, GREEN, self.rect_ground_collition)
            pygame.draw.rect(screen, GREEN, self.rect_head_collition)
            
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)


    def events(self, delta_ms, keys):
        self.elapsed_time_jump += delta_ms

        if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.walk(DIRECTION_L)

        if not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            self.walk(DIRECTION_R)

        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]:
            self.idle()

        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]:
            self.idle()

        if keys[pygame.K_SPACE]:
            if (self.elapsed_time_jump - self.time_last_jump) > self.interval_time_jump:
                self.jump(True)
                self.time_last_jump = self.elapsed_time_jump 
        
        if keys[pygame.K_f] and self.ready:
            self.shoot()
            print("entre")
            self.ready = False
            self.bullet_time = pygame.time.get_ticks()
        