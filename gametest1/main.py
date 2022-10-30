import pygame
from pygame.locals import *
import sys
import time

pygame.font.init()

textfont = pygame.font.SysFont("monospace", 15)
WIDTH = 500
HEIGHT = 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
WHITE = (255, 255, 255)
KASUGA_WIDTH, KASUGA_HEIGHT = 70, 100
WALKSPEED = 2

PLAYER = pygame.image.load('ichiban.png')
ICHIHOUSE = pygame.transform.scale(pygame.image.load('ichihouse.png'), (WIDTH, HEIGHT))
NANBA = pygame.image.load('nanba.png')
NANBANPC = pygame.transform.scale(NANBA, (KASUGA_WIDTH, KASUGA_HEIGHT))
KASUGA = pygame.transform.scale(PLAYER, (KASUGA_WIDTH, KASUGA_HEIGHT))


NANBAINTERACTIONTEXT = textfont.render("Yo, Ichi! Welcome to your game! Press E to learn more.", 1, WHITE)
NANBASECONDARYTEXT = textfont.render("Press E to learn more.", 1, WHITE)
NANBAMAINTEXT = textfont.render("This game is a work in progress. Just testing things for now", 10, WHITE)


def draw_window(kasugahitbox, nanbahitbox, keys_pressed):
    SCREEN.blit(ICHIHOUSE, (0, 0))
    SCREEN.blit(KASUGA, (kasugahitbox.x, kasugahitbox.y))
    SCREEN.blit(NANBANPC, (nanbahitbox.x, nanbahitbox.y))
    if kasugahitbox.x >= nanbahitbox.x - 100 and kasugahitbox.y >= nanbahitbox.y - 100:
            SCREEN.blit(NANBAINTERACTIONTEXT, (nanbahitbox.x- 100, nanbahitbox.y - 50))
            SCREEN.blit(NANBASECONDARYTEXT, (nanbahitbox.x - 100, nanbahitbox.y + 70))

    if keys_pressed[pygame.K_e] and kasugahitbox.x >= nanbahitbox.x - 100 and kasugahitbox.y >= nanbahitbox.y - 100:
            SCREEN.blit(NANBAMAINTEXT, (20, 100))
    pygame.display.update()
def main():
    kasugahitbox = pygame.Rect(50, 50, KASUGA_WIDTH, KASUGA_HEIGHT)
    nanbahitbox = pygame.Rect(300, 300, KASUGA_WIDTH, KASUGA_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:
            kasugahitbox.x -= WALKSPEED
        if keys_pressed[pygame.K_d]:
           kasugahitbox.x += WALKSPEED
        if keys_pressed[pygame.K_w]:
           kasugahitbox.y -= WALKSPEED
        if keys_pressed[pygame.K_s]:
           kasugahitbox.y += WALKSPEED
        
        draw_window(kasugahitbox, nanbahitbox, keys_pressed)
    pygame.quit()

main()