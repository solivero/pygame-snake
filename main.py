import pygame

GAME_NAME = 'Snake'
WIDTH = 800
HEIGHT = 600
FPS = 30

pygame.init()

game_display = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.update()
pygame.display.set_caption(GAME_NAME)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game_display.fill((255,255,255))
    # display, color, x y width height
    pygame.draw.rect(game_display, (0,0,0), [WIDTH/2-40/2,HEIGHT/2-80/2,40,80])
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
