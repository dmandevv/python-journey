import pygame
import random
from pygame.math import Vector2

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height, base_speed, acceleration_range):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_frect()
        self.rect.x = x
        self.rect.y = y

        self.base_speed = base_speed
        self.speed = base_speed
        self.acceleration_range = acceleration_range
        self.velocity = pygame.Vector2(-1, 1)
        self.score_pause_timer = 0

    def update(self, dt):
        if self.score_pause_timer > 0:
            self.score_pause_timer = max(0, self.score_pause_timer - dt)
            return
        self.rect.center += self.velocity * self.speed * dt

    def speed_up(self):
        self.speed += random.uniform(self.acceleration_range.x, self.acceleration_range.y)

    def reset(self, x, y, score_pause_time):
        self.rect.center = (x, y)
        self.velocity.x *= -1
        self.speed = self.base_speed
        self.score_pause_timer = score_pause_time
        