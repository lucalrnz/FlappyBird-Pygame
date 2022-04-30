import pygame
from .constants import SCREEN_WIDTH

class Ground(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 8
        self.img = pygame.image.load("flappybird/assets/sprites/base.png")
        self.y = 800
        self.x = x
        self.rect = self.img.get_rect()

    def draw(self, win):
        win.blit(self.img,(self.x, self.y))
    
    def move(self):
        self.x -= self.speed
        if self.x + self.img.get_width() < 0:
            self.x = 1000

    def update(self, win, game_over):
        if not game_over:
            self.move()
        self.draw(win)

