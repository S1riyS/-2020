import pygame
n = int(input("Введите ширину поля - "))
cross = 0
zero = 0

WIDTH = HEIGHT =600  # ширина и высота игрового окна
FPS = 60  # частота кадров в секунду

BLACK = (20, 20, 20)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tik-Tak-Toe")
clock = pygame.time.Clock()

run = True
r = WIDTH // n

def start_pos():
    screen.fill(BLACK)
    global tap, main, i, WIDTH, n
    tap = 1
    main = [[0 for i in range(n)] for i in range(n)]
    for i in range(n + 1):
        l = i * (WIDTH // n)
        pygame.draw.line(screen, WHITE, [0, l], [WIDTH, l], 3)
        pygame.draw.line(screen, WHITE, [l, 0], [l, HEIGHT], 3)

start_pos()

while run:
    if tap == n * n + 1:
        print("Ничья")
        start_pos()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(n + 1):
                    if (event.pos[0] > i * r)and (event.pos[0] < (i + 1) * r):
                        x_now = i
                    if (event.pos[1] > i * r) and  (event.pos[1] < (i + 1) * r):
                        y_now = i

            if main[y_now][x_now] == 0:

                tap += 1

                if tap % 2 == 0:
                    main[y_now][x_now] = 1
                    pygame.draw.line(screen, RED, [x_now * r, y_now * r],
                                     [(x_now + 1) * r, (y_now + 1) * r], 3)

                    pygame.draw.line(screen, RED, [x_now * r, (y_now + 1) * r],
                                     [(x_now + 1) * r, y_now * r], 2)
                else:
                    main[y_now][x_now] = -1
                    x = x_now * r + r // 2
                    y = y_now * r + r // 2
                    pygame.draw.circle(screen, BLUE, [x, y], r // 2, 3)

    # Расчерчиваем поле
    for i in range(n + 1):
        l = i * (WIDTH // n)
        pygame.draw.line(screen, WHITE, [0, l], [WIDTH, l], 3)
        pygame.draw.line(screen, WHITE, [l, 0], [l, HEIGHT], 3)

    tik = 0
    tik_diagonal = 0

    for i in range(len(main)):
        tik += main[i][i]
        a = main[i][::-1]
        tik_diagonal += a[i]

    if tik == -n or tik_diagonal == -n:
        print("Победели нолики")
        start_pos()
        zero += 1
    elif tik == n or tik_diagonal == n:
            print("Победили крестики")
            start_pos()
            cross += 1

    for i in main:

        if sum(i) == -n:
            print("Победели нолики")
            start_pos()
            zero += 1

        elif sum(i) == n:
            print("Победили крестики")
            start_pos()
            cross += 1


    pygame.display.flip()

pygame.quit()
print(zero, cross)