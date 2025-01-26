import pygame
import time
import random

# Инициализация Pygame
pygame.init()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Размеры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Частота обновления
clock = pygame.time.Clock()
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def show_score(score):
    value = score_font.render(f"Ваш счет: {score}", True, GREEN)
    screen.blit(value, [10, 10])

def message(msg, color):
    msg_surface = font_style.render(msg, True, color)
    screen.blit(msg_surface, [WIDTH // 6, HEIGHT // 3])


def game():
    game_over = False
    game_close = False

    x, y = WIDTH // 2, HEIGHT // 2
    x_change, y_change = 0, 0

    snake_list = []
    snake_length = 1

    # Координаты еды
    food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10
    food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10

    while not game_over:
        while game_close:
            screen.fill(BLACK)
            message("Игра окончена! Нажмите Q для выхода или C для перезапуска", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -SNAKE_BLOCK
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = SNAKE_BLOCK
                    x_change = 0

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        for block in snake_list:
            pygame.draw.rect(screen, BLUE, [block[0], block[1], SNAKE_BLOCK, SNAKE_BLOCK])

        show_score(snake_length - 1)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10
            food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

if __name__ == "__main__":
    game()
