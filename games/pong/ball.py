import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height, speed, up_key, down_key):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_frect()
        self.rect.x = x
        self.rect.y = y

        self.speed = speed
        self.up_key = up_key
        self.down_key = down_key

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[self.up_key]:
            self.rect.y -= self.speed * dt
        elif keys[self.down_key]:
            self.rect.y += self.speed * dt

    def in_bounds(self) -> bool:
        return True