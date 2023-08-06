import pygame
from random import randint, choice
import random

# pygame setup
pygame.init()
width, height = 1280, 680
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)  # Set the RESIZABLE flag
pygame.display.set_caption("Brick Breaker")
clock = pygame.time.Clock()
running = True
dt = 0

# load font for win/lose message display
pygame.font.init()
font = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 20)

# score setup, get high_score from file
score = 0

try:
    score_file = open("high_score.txt", "r")
    high_score = int(score_file.read().strip("\n"))
    score_file.close()
except:
    high_score = 0 # if no previous score

# colors
TEAL = (0, 128, 128)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
PINK = (255, 105, 180)
font = pygame.font.SysFont(None, 50, bold=True)

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
welcome_bricks = []

for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * (brick_width + padding) + 10
        brick_y = row * (brick_height + padding) + 50
        # Generate random RGB values for the brick color
        brick_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        welcome_bricks.append((pygame.Rect(brick_x, brick_y, brick_width, brick_height), brick_color))

# play again / quit buttons
def end_game_screen(end_game_type):
    # pass the condition on which game ended (win or game_over)
    # create PLAY AGAIN and QUIT buttons
    play_again_text = font.render("PLAY AGAIN", True, WHITE)
    quit_text = font.render("QUIT", True, WHITE)

    # get coordinates to display in same line
    button_padding = 35  # space between buttons
    total_button_width = play_again_text.get_width() + quit_text.get_width() + button_padding
    button_start_x = (width - total_button_width) // 2
    play_again_rect = play_again_text.get_rect(left = button_start_x, top = height // 2 + 50)
    quit_rect = quit_text.get_rect(left = button_start_x + play_again_text.get_width() + button_padding, top = height // 2 + 50)

    screen.blit(play_again_text, play_again_rect)
    screen.blit(quit_text, quit_rect)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    # play again logic
    if event.type == pygame.MOUSEBUTTONDOWN:
        if play_again_rect.collidepoint(mouse_x, mouse_y):
            # reset game
            global score, player_x, player_y, ball_x, ball_y, ball_dx, ball_dy, bricks, running
            if end_game_type == "win":
                global win
                win = False

            if end_game_type == "game_over":
                global game_over
                game_over = False

            score = 0

            player_x = (width - player_width) // 2
            player_y = screen.get_height() / 1.2

            ball_x = width // 2
            ball_y = player_y - ball_radius
            ball_dx = choice([-2, 2])
            ball_dy = -2

            bricks.clear()
            for row in range(brick_rows):
                for col in range(brick_cols):
                    brick_x = col * (brick_width + padding) + 10
                    brick_y = row * (brick_height + padding) + 50
                    bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

    # quit logic
    if event.type == pygame.MOUSEBUTTONDOWN:
        if quit_rect.collidepoint(mouse_x, mouse_y):
            running = False

def welcome_screen():
    screen.fill(BLACK)
    # Draw bricks for the welcome screen
    for brick, color in welcome_bricks:
        pygame.draw.rect(screen, color, brick)
        pygame.draw.rect(screen, BLACK, brick, 1)  # Brick outlines for padding
    
    brick_breaker = font.render("BRICK BREAKER!", True, PINK)
    # Draw play and quit buttons
    play_button_text = font.render("PLAY", True, WHITE)
    quit_button_text = font.render("QUIT", True, WHITE)

    button_padding = 35  # space between buttons
    total_button_width = play_button_text.get_width() + quit_button_text.get_width() + button_padding
    button_start_x = (width - total_button_width) // 2

    text_rect = brick_breaker.get_rect(center=(width // 2, height // 2))
    play_button_rect = play_button_text.get_rect(left=button_start_x, top=height // 2 + 50)
    quit_button_rect = quit_button_text.get_rect(left=button_start_x + play_button_text.get_width() + button_padding,
                                                 top=height // 2 + 50)

    screen.blit(brick_breaker, text_rect)
    screen.blit(play_button_text, play_button_rect)
    screen.blit(quit_button_text, quit_button_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if play_button_rect.collidepoint(mouse_x, mouse_y):
                    return
                if quit_button_rect.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    quit()


game_over = False
win = False
welcome_screen()

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
        elif event.type == pygame.VIDEORESIZE:  # Handle resize event
            width, height = event.w, event.h
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BLACK)

    if not (game_over or win):
        # draw player (paddle)
        pygame.draw.rect(screen, TEAL, (player_x, player_y, player_width, player_height))

        # draw ball
        pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

        # draw bricks
        for brick in bricks:
            pygame.draw.rect(screen, brick_color, brick)
            pygame.draw.rect(screen, BLACK, brick, 1)  # brick outlines for padding

        # display score
        high_score_text = score_font.render(f"HIGH SCORE: {high_score}", True, WHITE)
        screen.blit(high_score_text, (10, height - high_score_text.get_height() - 50))

        score_text = score_font.render(f"SCORE: {score}", True, WHITE)
        screen.blit(score_text, (10, height - high_score_text.get_height() - 30))

        # move player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= 300 * dt * player_speed
        if keys[pygame.K_RIGHT]:
            player_x += 300 * dt * player_speed

        # <----- move ball ----->
        ball_x += ball_dx * ball_speed
        ball_y += ball_dy * ball_speed

        # update ball rect with new coordinates
        ball = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)

        # collision detection with walls
        if ball_x <= ball_radius or ball_x >= width - ball_radius:
            ball_dx *= -1
        if ball_y <= ball_radius:
            ball_dy *= -1

        # collision detection with player
        if ball.colliderect(pygame.Rect(player_x, player_y, player_width, player_height)):
            ball_dy *= -1

        # collision detection with bricks
        for brick in bricks:
            if ball.colliderect(brick):
                bricks.remove(brick) # destroy brick
                ball_dy *= -1
                # change brick colors on hit (select random rgb values using randint)
                brick_color = (randint(0, 255), randint(0, 255), randint(0, 255))
                score += 1

        # game over condition
        if ball_y > height:
            game_over = True

        # win condition
        if len(bricks) == 0:
            win = True

    # save high score to file
    if win or game_over:
        if score > high_score:
            score_file = open("high_score.txt", "w")
            score_file.write(str(score))
            score_file.close()

    # game over screen
    if game_over:
        game_over_text = font.render("GAME OVER", True, RED)
        screen.blit(game_over_text, ((width - game_over_text.get_width()) // 2, height // 2))
        end_game_screen("game_over")

    # win screen
    if win:
        win_text = font.render("WIN", True, GREEN)
        screen.blit(win_text, ((width - win_text.get_width()) // 2, height // 2))
        end_game_screen("win")

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
