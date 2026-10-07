"""
Pong for two players at one keyboard.

Left paddle: W / S.  Right paddle: Up / Down.  Quit: close the window or Esc.

Play:  .venv/bin/python games/pong/pong.py
"""
import pygame
from paddle import Paddle

WIDTH, HEIGHT = 800, 600
FPS = 144
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 70
PADDLE_SPEED = 300

WALL_THICKNESS = 50

def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()

    paddle1 = Paddle(pygame.Color("white"), PADDLE_WIDTH // 2, HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED, pygame.K_w, pygame.K_s)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(paddle1)

    walls = [
        pygame.Rect(0, -WALL_THICKNESS, WIDTH, WALL_THICKNESS), #top
        pygame.Rect(0, HEIGHT, WIDTH, WALL_THICKNESS), #bottom
        pygame.Rect(-WALL_THICKNESS, 0, WALL_THICKNESS, HEIGHT), #left
        pygame.Rect(WIDTH, 0, WALL_THICKNESS, HEIGHT), #right
    ]

    running = True
    while running:
        dt = clock.tick(FPS) / 1000

        # 1. Events: things that happened since the last frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # 2. Update: move things, check collisions, keep score
        all_sprites.update(dt)
        if (i := paddle1.rect.collidelist(walls)) != -1:
            wall = walls[i]
            if wall is walls[0]:                    # top
                paddle1.rect.top = wall.bottom
            elif wall is walls[1]:                  # bottom
                paddle1.rect.bottom = wall.top


        # 3. Draw: clear the screen, draw everything, then show it
        screen.fill("black")
        all_sprites.draw(screen)
        pygame.display.flip()
        

    pygame.quit()


if __name__ == "__main__":
    main()
