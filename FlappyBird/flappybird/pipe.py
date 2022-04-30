import pygame
import random
from .constants import GREEN, SCREEN_HEIGHT

class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 8
        self.height_bottom = random.randint(300, 750)
        self.height_top = self.height_bottom - 200
        self.x = 860
        self.img = pygame.image.load("flappybird/assets/sprites/pipe-green.png")
        self.img = pygame.transform.scale(self.img,(int(self.img.get_width() * 2.5), int(self.img.get_height() * 2.5)))
        self.rect_top = None
        self.rect_bottom = None
        self.passed = False
        
   
    
    def draw(self, win):
        win.blit(self.img, (self.x, self.height_bottom))
        self.rect_bottom = pygame.Rect(self.x, self.height_bottom, self.img.get_width(), self.img.get_height())
        win.blit(pygame.transform.rotate(self.img, 180), (self.x, int(self.height_top - self.img.get_height())))
        self.rect_top = pygame.Rect(self.x, int(self.height_top - self.img.get_height()), self.img.get_width(), self.img.get_height())
    
    def move(self):
        self.x -= self.speed
        if self.x + 150 < 0:
            self.kill()
        
        self.rect = pygame.Rect(self.x, self.height_bottom, 130, SCREEN_HEIGHT - self.height_bottom)
        
        
    def update(self, win, game_over):
        if not game_over:
            self.move()
        self.draw(win)
    