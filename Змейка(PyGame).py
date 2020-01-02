import pygame
import random

file1 = open("Record.txt", "r")
for i in file1:
    record = int(i)
file1.close()

file2 = open("Record.txt", 'w')

right = up = down = r = False
left = True

WIDTH = 520  # ширина игрового окна
HEIGHT = 520  # высота игрового окна
FPS = 10  # частота кадров в секунду

BLACK = (12, 12, 12)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

apple_mass = [i for i in range(20, WIDTH - 39, 20)]

apple_x = random.choice(apple_mass)
apple_y = random.choice(apple_mass)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT + 50))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

main_x = WIDTH // 2
main_y = HEIGHT // 2
start_pos = [[260, 300], [280, 300], [300, 300]]
positions = [[260, 300], [280, 300], [300, 300]]


# Цикл игры
run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():

        x_now = positions[0][0]
        y_now = positions[0][1]

        if event.type == pygame.QUIT:
            if r:
                file2.write(str(len(positions)))
            else:
                file2.write(str(record))
            run = False

        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not right:
                    left = True
                    right = up = down = False
                elif event.key == pygame.K_RIGHT and not left:
                    right = True
                    left = up = down = False
                elif event.key == pygame.K_UP and not down:
                    up = True
                    left = right = down = False
                elif event.key == pygame.K_DOWN and not up:
                    down = True
                    left = right = up = False
                else:
                    continue

    if 0 <= positions[0][0] <= WIDTH and 0 <= positions[0][1] <= HEIGHT and positions.count([x_now, y_now]) <= 1:
        if left:
            x_now -= 20
        elif right:
            x_now += 20
        elif up:
            y_now -= 20
        elif down:
            y_now += 20
        positions.insert(0, [x_now, y_now])
        del positions[len(positions) - 1]
        screen.fill(BLACK)
    else:
        if r:
            file2.write(str(len(positions)))
        else:
            file2.write(str(record))
        run = False

    for i in range(len(positions)):
        if i == 0:
            color = (200, 200, 200)
        else:
            color = WHITE
        main = pygame.draw.rect(screen, color, (positions[i][0], positions[i][1], 20, 20))
        main_out = pygame.draw.rect(screen, BLACK, (positions[i][0], positions[i][1], 20, 20), 1)

    apple = pygame.draw.rect(screen, GREEN, (apple_x, apple_y, 20, 20))

    if positions[0][0] == apple_x and positions[0][1] == apple_y:
        x = positions[len(positions) - 1][0]
        y = positions[len(positions) - 1][1]
        positions.append([x, y])
        apple_x = random.choice(apple_mass)
        apple_y = random.choice(apple_mass)

        while [apple_x, apple_y] in positions:
            apple_x = random.choice(apple_mass)
            apple_y = random.choice(apple_mass)

    out = pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, HEIGHT), 4)
    out_bg = pygame.draw.rect(screen, BLACK, (0, 520, 520, 600))

    if len(positions) > record:
        r = True
        record = len(positions)
    font = pygame.font.Font(None, 32)
    result = font.render('Длинна змейки:  ' + str(len(positions)), 1, WHITE)
    screen.blit(result, (20, 535))

    record_str = font.render('Рекорд:  ' + str(record), 1, WHITE)
    screen.blit(record_str, (300, 535))

    pygame.display.flip()

pygame.quit()