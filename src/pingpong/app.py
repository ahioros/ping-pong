import pygame

from pingpong.ball import Ball
from pingpong.paddle import Paddle


def main():

    # Window dimensions
    WIDTH = 640
    HEIGHT = 480

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Init
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ping Pong")

    clock = pygame.time.Clock()

    # Instances creation
    paddle1 = Paddle(10, (HEIGHT // 2) - 30, HEIGHT, WHITE)
    paddle2 = Paddle(WIDTH - 20, (HEIGHT // 2) - 30, HEIGHT, WHITE)
    ball = Ball(HEIGHT, WIDTH, WHITE)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.move_up()
        if keys[pygame.K_s]:
            paddle1.move_down()
        if keys[pygame.K_UP]:
            paddle2.move_up()
        if keys[pygame.K_DOWN]:
            paddle2.move_down()

        ball.update()

        # Collision
        if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
            ball.vel[0] = -ball.vel[0]

        screen.fill(BLACK)
        paddle1.draw(screen)
        paddle2.draw(screen)
        ball.draw(screen)

        pygame.display.update()
        clock.tick(60)

        # Quit
        if keys[pygame.K_q] or keys[pygame.K_ESCAPE]:
            running = False
            pygame.quit()

    pygame.quit()


if __name__ == "__main__":
    main()
