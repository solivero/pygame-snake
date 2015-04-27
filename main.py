import pygame
import random

GAME_NAME = 'Gridder'
WIDTH = 800
HEIGHT = 600
FPS = 30

pygame.init()

game_display = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.update()
pygame.display.set_caption(GAME_NAME)

clock = pygame.time.Clock()
running = True

circle_size = 40
rows = 12
cols = 16

dots = []
# init list with rows of colors
for i in range(rows):
    row = []
    for j in range(cols):
        row.append((i*2,j*2,i*j))
    dots.append(row)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game_display.fill((255,255,255))
    # display, color, x y width height
    # draw circles in grid
    current_y = 0

    for row in dots:
        current_x = 0
        current_y += circle_size + 5
        for dot in row:
            current_x += circle_size + 5
            pygame.draw.rect(game_display, dot, [current_x, current_y, circle_size, circle_size])

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
