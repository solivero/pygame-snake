import pygame
import random

GAME_NAME = 'Snake'
WIDTH = 800
HEIGHT = 600
FPS = 10

pygame.init()

game_display = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.update()
pygame.display.set_caption(GAME_NAME)

clock = pygame.time.Clock()
font_size = 40
font = pygame.font.SysFont(None, font_size)
running = True
block_size = 40
def game_over(score):
    lines = ["Game Over", "Score "+str(score), "Hit Space to play again"]
    for i in range(len(lines)):
        # GET REKT!!
        text = font.render(lines[i], True, (200, 20, 20))
        line_width = text.get_rect()[2]
        line_height = text.get_rect()[3]
        game_display.blit(text, [WIDTH/2-line_width/2, HEIGHT/2-line_height/2+font_size*i+3])
    pygame.display.update()
#lyssna efter space
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_game()
            elif event.type == pygame.QUIT:
                pygame.quit()

def draw_snake(snake):
    # Rita svansen block för block
    for block in snake[:-1]:
        pygame.draw.rect(game_display, (0, 0, 0), [block[0], block[1], block_size, block_size])
    pygame.draw.rect(game_display, (40, 200, 80), [snake[-1][0], snake[-1][1], block_size, block_size])

def start_game():
    start_x = 8*block_size
    start_y = 8*block_size
# Börja åt höger
    change_x = block_size
    change_y = 0
    score = 0
# Matbit (block) på random plats, inom samma möjliga koordinater som ormen
    food = (random.randrange(WIDTH/block_size)*block_size,
            random.randrange(HEIGHT/block_size)*block_size)
    food_color = (0, 0, 255)
# Ormen är en lista av sammanhängande block (x,y)
    snake = []
    for i in range(6):
        snake.append((start_x+block_size*i, start_y+block_size))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
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
        if snake[-1][0] > WIDTH or snake[-1][0] < 0 or snake[-1][1] > HEIGHT or snake[-1][1] < 0:
            game_over(score)
            break
        # Kolla om ormens huvud är på samma plats som matbiten
        if snake[-1][0] == food[0] and snake[-1][1] == food[1]:
            snake.append((snake[-1][0]+change_x, snake[-1][1]+change_y))
            food = (random.randrange(WIDTH/block_size)*block_size,
                    random.randrange(HEIGHT/block_size)*block_size)
            food_color = (random.randrange(200),random.randrange(200),random.randrange(200))
            score += 1

        game_display.fill((255,255,255))
        pygame.draw.rect(game_display,
                         food_color,
                         [food[0], food[1], block_size, block_size])
        draw_snake(snake)

        pygame.display.update()
        clock.tick(FPS)

start_game()
pygame.quit()
quit()
