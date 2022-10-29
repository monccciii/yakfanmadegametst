import pygame
from pygame.locals import *
import sys
WIDTH = 1000
HEIGHT = 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
WHITE = (255, 255, 255)
KASUGA_WIDTH, KASUGA_HEIGHT = 100, 50

IMG = pygame.image.load('ichiban.png')
KASUGA = pygame.transform.scale(IMG, (KASUGA_WIDTH, KASUGA_HEIGHT))


def draw_window():
    SCREEN.fill(WHITE)
    SCREEN.blit(KASUGA, (50, 50))
    pygame.display.update()
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()
    pygame.quit()

main()