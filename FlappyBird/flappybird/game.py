import pygame
from .constants import *
from .bird import Bird
from .pipe import Pipe
from .ground import Ground
from .button import Button

class Game():
    def __init__(self, win):
        self._init()

        #load images
        self.background = pygame.image.load("flappybird/assets/sprites/background-day.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
        self.gameover_img = pygame.image.load("flappybird/assets/sprites/gameover.png").convert_alpha()
        self.gameover_img = pygame.transform.scale(self.gameover_img, (self.gameover_img.get_width() * 2, self.gameover_img.get_height() * 2))
        self.restart_button_img = pygame.image.load("flappybird/assets/sprites/restart_button.png").convert_alpha()

        self.game_over_button = Button(int(SCREEN_WIDTH // 2) - int(self.restart_button_img.get_width() * 0.5 // 2), int(SCREEN_HEIGHT // 2) + 40, self.restart_button_img, 0.5)
        self.bird = Bird()
        self.win = win
        self.ground_group = pygame.sprite.Group()
        self.create_ground()
        self.pipe_group = pygame.sprite.Group()

    def _init(self):
        self.pipe_spawn = 0
        self.score = 0
        self.game_over = False

    def draw_background(self):
        self.win.blit(self.background, (0, 0))
    
    def update(self):
        self.pipe_spawn -= 1
        self.draw_background()
        self.create_pipes()
        self.pipe_group.update(self.win, self.game_over)
        self.ground_group.update(self.win, self.game_over)
        self.bird.update(self.win)
        self.display_score()

        #check for collision between bird and pipes
        for pipe in self.pipe_group:
            if self.bird.rect.colliderect(pipe.rect_bottom):
                self.bird.vel = 25
                self.game_over = True
            elif self.bird.rect.colliderect(pipe.rect_top):
                self.bird.vel = 25
                self.game_over = True
            if pipe.x + pipe.img.get_width() < self.bird.x and not pipe.passed:
                pipe.passed = True
                self.score += 1
        
        #check for collision with the ground
        if self.bird.y >= 700:
            self.game_over = True
        
        if self.game_over:
            self.handle_gameover()

    def create_pipes(self):
        if self.bird.moved and self.pipe_spawn <= 0:
            pipe = Pipe()
            self.pipe_group.add(pipe)
            self.pipe_spawn = 40
        
    def create_ground(self):
        ground = Ground(0)
        self.ground_group.add(ground)
        ground2 = Ground(ground.x + ground.img.get_width())
        self.ground_group.add(ground2)
        ground3 = Ground(ground2.x + ground2.img.get_width())
        self.ground_group.add(ground3)
        ground4 = Ground(ground3.x + ground3.img.get_width())
        self.ground_group.add(ground4)

    def display_score(self):
        x = [int(a) for a in str(self.score)]
        for i in range(len(x)):
            digit = int(x[i])
            self.win.blit(pygame.image.load(f"flappybird/assets/sprites/{digit}.png"), (15 + 25 * i, 15))
    
    def reset(self):
        self._init()
        self.bird.reset()

    def handle_gameover(self):
        self.win.blit(self.gameover_img, (int(SCREEN_WIDTH // 2) - int(self.gameover_img.get_width() // 2), int(SCREEN_HEIGHT // 2) - 120))
        if self.game_over_button.draw(self.win):
            self.reset()
            self.pipe_group.empty()
    

