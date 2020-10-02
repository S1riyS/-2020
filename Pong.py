import pygame
import random
import math
pygame.init()

#----- КОНСТАНТЫ -----
BLACK = (12, 12, 12)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 1020  # ширина игрового окна
HEIGHT = 620  # высота игрового окна
FPS = 60  # частота кадров в секунду

#----- ОТРИСОВКА ОКНА -----
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping-Pong")
clock = pygame.time.Clock()

# Rackets
racket_width = 10
racket_height = 100

#---- Racket 1
up_btn_1 = pygame.K_w
down_btn_1 = pygame.K_s

#---- Racket 2
up_btn_2 = pygame.K_UP
down_btn_2 = pygame.K_DOWN

# Ball
ball_width = ball_height = 15
img_ball = pygame.image.load('bird.png')


# Functions
class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.color = color


class Racket(GameObject):
    def __init__(self, x, y, speed, up_button, down_button, w=racket_width, h=racket_height, color=WHITE):
        super().__init__(x, y, w, h, color)

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

        self.rect.x = self.x
        self.speed = speed

        self.up_button = up_button
        self.down_button = down_button

    def update(self):
            self.speedY = 0
            keystate = pygame.key.get_pressed()
            if keystate[self.up_button]:
                if not self.rect.y < 0:
                    self.speedY = -self.speed
            if keystate[self.down_button]:
                if not self.rect.y + self.height > HEIGHT:
                    self.speedY = self.speed
            self.rect.y += self.speedY


class Ball(GameObject):
    def __init__(self, x, y, speedX, speedY, w=ball_width, h=ball_height, color=WHITE):
        super().__init__(x, y, w, h, color)
        self.speedX = speedX
        self.speedY = speedY

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def restart(self):
        self.rect.x = self.x
        self.rect.y = self.y
        print(self.x, self.y)

    def edges(self):
        if self.rect.y < 0 or self.rect.y > HEIGHT:
            self.speedY *= -1

        if self.rect.x < 0 or self.rect.x > WIDTH:
            self.restart()
            print(self.x, self.y)


    def update(self):
        self.edges()
        self.rect.x += self.speedX
        self.rect.y += self.speedY


all_sprites = pygame.sprite.Group()

racket_left = Racket(15, HEIGHT // 2, 15, up_btn_1, down_btn_1)
racket_right = Racket(WIDTH - (racket_width + 15), HEIGHT // 2, 15, up_btn_2, down_btn_2)
ball = Ball(WIDTH // 2, HEIGHT // 2, 10, 5)

all_sprites.add(racket_left, racket_right, ball)

# Game parameters
game = True
keys = pygame.key.get_pressed()

while game:
    clock.tick(FPS)
    all_sprites.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    # Отрисовка
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
