import pygame
import sys

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height, speed):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_frect()
        self.rect.x = x
        self.rect.y = y

        self.speed = speed

    def update(self, dt):
        self.rect.y += self.get_direction() * self.speed * dt

    def get_direction(self) -> int:
        raise NotImplementedError

    def in_bounds(self) -> bool:
        return True

class PlayerPaddle(Paddle):
    def __init__(self, color, x, y, width, height, speed, up_key, down_key):
        super().__init__(color, x, y, width, height, speed)
        self.up_key = up_key
        self.down_key = down_key

    def get_direction(self) -> int:
        keys = pygame.key.get_pressed()
        return keys[self.down_key] - keys[self.up_key]

class ComputerPaddle(Paddle):
    def __init__(self, color, x, y, width, height, speed, ball):
        super().__init__(color, x, y, width, height, speed)
        self.ball = ball
    def get_direction(self) -> int:
        if self.ball.rect.y > self.rect.y:
            return 1
        if self.ball.rect.y < self.rect.y:
            return -1
        return 0