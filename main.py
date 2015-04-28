import pygame

GAME_NAME = 'Snake'
WIDTH = 800
HEIGHT = 600
FPS = 10

pygame.init()

game_display = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.update()
pygame.display.set_caption(GAME_NAME)

clock = pygame.time.Clock()
running = True

block_size = 40
start_x = 300
start_y = 300
# Börja åt höger
change_x = block_size
change_y = 0

# Ormen är en lista av sammanhängande block (x,y)
snake = []
for i in range(6):
    snake.append((start_x+block_size*i, start_y+block_size))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_y = -block_size
                change_x = 0
            elif event.key == pygame.K_DOWN:
                change_y = block_size
                change_x = 0
            elif event.key == pygame.K_LEFT:
                change_x = -block_size
                change_y = 0
            elif event.key == pygame.K_RIGHT:
                change_x = block_size
                change_y = 0
    # Lägg till nytt block och ta bort sista (svansen)
    snake.append((snake[-1][0]+change_x, snake[-1][1]+change_y))
    del snake[0]

    # Kolla om ormen åker utanför spelplanen
    if snake[-1][0] > WIDTH or snake[-1][0] < 0:
        pygame.quit()
    if snake[-1][1] > HEIGHT or snake[-1][1] < 0:
        pygame.quit()

    game_display.fill((255,255,255))
    # Rita ormen block för block
    for block in snake:
        pygame.draw.rect(game_display, (0, 0, 0), [block[0], block[1], block_size, block_size])
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
