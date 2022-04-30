from shutil import move
import pygame
from .constants import YELLOW

class Bird():
    def __init__(self):
        self._init()
        self.animation_list = []
        for i in range(4):
            small_img = pygame.image.load(f"flappybird/assets/sprites/bird/{i}.png")
            img = pygame.transform.scale(small_img, (int(small_img.get_width() * 2), int(small_img.get_height() * 2)))
            self.animation_list.append(img)
        self.img = self.animation_list[0]
        self.rect = self.img.get_rect()
        self.max_rotation = 25

    def _init(self):
        self.x = 270
        self.y = 460
        self.vel = 0
        self.tick_count = 0
        self.height = self.y
        self.moved = False
        self.tilt = 0
        self.animation_index = 0
        self.animation_cooldown = 3

    def draw(self, win):
        self.img = pygame.transform.rotate(self.img,  self.tilt)
        win.blit(self.img, (self.x, self.y))
    
    def update(self, win):
        self.move()
        self.update_animation()
        self.draw(win) 
        self.animation_cooldown -= 1

    def jump(self):
        self.moved = True
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y
    
    def update_animation(self):
        if self.animation_cooldown <= 0:
            if self.animation_index >= len(self.animation_list) - 1:
                self.animation_index = 0
            else:
                self.animation_index += 1
            self.animation_cooldown = 3
        self.img = self.animation_list[self.animation_index]
       
    def move(self):
        if self.moved:
            self.tick_count += 1

            movement = self.vel*(self.tick_count) + 0.5*(3)*self.tick_count**2

            if movement >= 16:
                movement = (movement/abs(movement)) * 16
            
            if movement < 0:
                movement -= 2
            
            self.y = self.y + movement
            self.rect = pygame.Rect(325 - 13, self.y + 13, 26, 26)

            if movement < 0 or self.y < self.height + 50:
                if self.tilt < self.max_rotation:
                    self.tilt = self.max_rotation
            else:
                if self.tilt > -90:
                    self.tilt -= 20
    
    def reset(self):
        self._init()
