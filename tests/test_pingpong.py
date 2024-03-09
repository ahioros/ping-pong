import pygame
import pytest
from pingpong.ball import Ball
from pingpong.paddle import Paddle
from pygame.locals import *

# Ball color
WHITE = (255, 255, 255)

# Dimensiones de la ventana del juego
WIDTH = 640
HEIGHT = 480


# Prueba unitaria para verificar que la paleta se mueva hacia arriba correctamente
def test_paddle_move_up():
    paddle = Paddle(10, 10, HEIGHT, WHITE)
    initial_y = paddle.rect.y
    paddle.move_up()
    assert paddle.rect.y == initial_y - 5


# Prueba unitaria para verificar que la paleta se mueva hacia abajo correctamente
def test_paddle_move_down():
    paddle = Paddle(10, 10, HEIGHT, WHITE)
    initial_y = paddle.rect.y
    paddle.move_down()
    assert paddle.rect.y == initial_y + 5


# Prueba unitaria para verificar que la pelota se actualice correctamente
def test_ball_update():
    ball = Ball(HEIGHT, WIDTH, WHITE)
    initial_pos = ball.rect.topleft
    ball.update()
    assert ball.rect.topleft != initial_pos


# Prueba unitaria para verificar la colisión entre la pelota y la paleta
def test_ball_paddle_collision():
    paddle = Paddle(10, 10, HEIGHT, WHITE)
    ball = Ball(HEIGHT, WIDTH, WHITE)
    ball.rect.x = 20
    ball.rect.y = 10
    initial_vel = ball.vel.copy()
    ball.update()
    assert ball.vel[0] == initial_vel[0]


# Ejecutar las pruebas
if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ping Pong")

    pytest.main(["-v"])
