import pygame
import os
import neat
from flappybird.constants import *
from flappybird.game import Game

WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        pygame.time.delay(30)
        clock.tick(FPS)
        game.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN and game.game_over != True:
                if event.key == pygame.K_SPACE:
                    game.bird.jump()
                
            if event.type == pygame.MOUSEBUTTONDOWN and game.game_over != True:
                game.bird.jump()
                    
        pygame.display.update()
    
    pygame.quit()

main()

