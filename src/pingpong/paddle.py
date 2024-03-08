import pygame


# Paddle Class
class Paddle:
    def __init__(self, x, y, HEIGHT, WHITE):
        self.HEIGHT = HEIGHT
        self.WHITE = WHITE
        self.rect = pygame.Rect(x, y, 10, 60)

    def move_up(self):
        if self.rect.top > 0:
            self.rect.move_ip(0, -5)

    def move_down(self):
        if self.rect.bottom < self.HEIGHT:
            self.rect.move_ip(0, 5)

    def draw(self, surface):
        pygame.draw.rect(surface, self.WHITE, self.rect)
