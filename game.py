import pygame
from random import choice

# pygame setup
pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Brick Breaker")
clock = pygame.time.Clock()
running = True
dt = 0

# colors
TEAL = (0, 128, 128)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 128, 0)

# set up the player
player_color = TEAL
player_width = 100
player_height = 10
player_x = (width - player_width) // 2
player_y = screen.get_height() / 1.2
player_speed = 2

# set up ball
ball_color = WHITE
ball_radius = 5
ball_x = width // 2
ball_y = player_y - ball_radius
ball_dx = choice([-2, 2])
ball_dy = -2
ball_speed = 2

# set up bricks
brick_color = ORANGE
brick_width = 100
brick_height = 30
brick_rows = 5
brick_cols = width // (brick_width + 5)
padding = 5
bricks = []  # contains the undestroyed bricks

for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * (brick_width + padding) + 10
        brick_y = row * (brick_height + padding) + 50
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

# game loop
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BLACK)

    # draw player (paddle)
    pygame.draw.rect(screen, TEAL, (player_x, player_y,
                    player_width, player_height))

    # draw ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # draw bricks
    for brick in bricks:
        pygame.draw.rect(screen, brick_color, brick)
        pygame.draw.rect(screen, BLACK, brick, 1)  # brick outlines for padding

    # move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 300 * dt * player_speed
    if keys[pygame.K_RIGHT]:
        player_x += 300 * dt * player_speed

    # <----- move ball ----->
    ball_x += ball_dx * ball_speed
    ball_y += ball_dy * ball_speed

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
