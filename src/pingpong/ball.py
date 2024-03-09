import pygame


# Clase Ball (pelota)
class Ball:
    def __init__(self, HEIGHT, WIDTH, WHITE):
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.WHITE = WHITE
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 10, 10)
        self.vel = [3, 3]

    def update(self):
        self.rect.move_ip(self.vel[0], self.vel[1])

        if self.rect.left < 0 or self.rect.right > self.WIDTH:
            self.vel[0] = -self.vel[0]

        if self.rect.top < 0 or self.rect.bottom > self.HEIGHT:
            self.vel[1] = -self.vel[1]

    def draw(self, surface):
        pygame.draw.ellipse(surface, self.WHITE, self.rect)
