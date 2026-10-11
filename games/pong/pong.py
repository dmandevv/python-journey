"""
Pong for two players at one keyboard.

Left paddle: W / S.  Right paddle: Up / Down.  Quit: close the window or Esc.

Play:  .venv/bin/python games/pong/pong.py
"""
import pygame
from pygame.math import Vector2
from paddle import PlayerPaddle, ComputerPaddle
from ball import Ball

WIDTH, HEIGHT = 800, 600
FPS = 144
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 70
PADDLE_SPEED = 300

WALL_THICKNESS = 50
SCORE_PAUSE_TIME = 2.0

def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()

    ball = Ball(pygame.Color("white"), WIDTH // 2, HEIGHT // 2, 10, 10, 200, Vector2(10, 50))
    paddle1 = PlayerPaddle(pygame.Color("white"), PADDLE_WIDTH // 2, HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED, pygame.K_w, pygame.K_s)
    paddle2 = ComputerPaddle(pygame.Color("white"), WIDTH - PADDLE_WIDTH, HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED, ball)    

    all_sprites = pygame.sprite.Group()
    all_sprites.add(paddle1, paddle2, ball)

    walls = [
        pygame.Rect(0, -WALL_THICKNESS, WIDTH, WALL_THICKNESS), #top
        pygame.Rect(0, HEIGHT, WIDTH, WALL_THICKNESS), #bottom
        pygame.Rect(-WALL_THICKNESS, 0, WALL_THICKNESS, HEIGHT), #left
        pygame.Rect(WIDTH, 0, WALL_THICKNESS, HEIGHT), #right
    ]

    score1 = score2 = 0
    font = pygame.font.Font(None, 64)
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
        if (i := paddle2.rect.collidelist(walls)) != -1:
            wall = walls[i]
            if wall is walls[0]:                    # top
                paddle2.rect.top = wall.bottom
            elif wall is walls[1]:                  # bottom
                paddle2.rect.bottom = wall.top
        if (i := ball.rect.collidelist(walls)) != -1:
            wall = walls[i]
            if wall is walls[0]:                    # top
                ball.velocity.y *= -1
                ball.rect.top = wall.bottom
            elif wall is walls[1]:                  # bottom
                ball.velocity.y *= -1
                ball.rect.bottom = wall.top
            elif wall is walls[2]:                  # left
                score2 += 1
                ball.reset(WIDTH / 2, HEIGHT / 2, SCORE_PAUSE_TIME)
            elif wall is walls[3]:                  # right
                score1 += 1
                ball.reset(WIDTH / 2, HEIGHT / 2, SCORE_PAUSE_TIME)
        if (ball.rect.colliderect(paddle1.rect)):
            ball.rect.left = paddle1.rect.right
            ball.velocity.x *= -1
            ball.speed_up()
        if (ball.rect.colliderect(paddle2.rect)):
            ball.rect.right = paddle2.rect.left
            ball.velocity.x *= -1
            ball.speed_up()

        # 3. Draw: clear the screen, draw everything, then show it
        screen.fill("black")
        all_sprites.draw(screen)
        text = font.render(f"{score1}   {score2}", True, "white")
        screen.blit(text, text.get_rect(midtop=(WIDTH / 2, 20)))
        pygame.display.flip()
        

    pygame.quit()


if __name__ == "__main__":
    main()
