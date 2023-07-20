# Brick Breaker

Classic break-breaker game clone made using pygame utilities. The program uses simple shape drawing methods and collision detection using screen dimensions and collision methods.
</br>

Default screen resolution is 1280x720:
```python
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
```

<hr>

## Score System
Each ball hit on brick increments the score by 1. High Score record is kept by saving and loading the high score in a file "high_score.txt".

```python
try:
    score_file = open("high_score.txt", "r")
    high_score = int(score_file.read().strip("\n"))
    score_file.close()
except:
    high_score = 0 # if no previous score
```
</br>
Both Score and High Score are displayed in the lower left corner of the screen when game is running:
</br></br>
<p align = "center">
   <img src="https://github.com/daimbk/brick-breaker/assets/51926730/4e1d686b-fd33-4ccf-ad09-c0e5f9e86e4a" width="798" height="351" border="15"/>
</p>

<hr>

## Paddle, Ball and Brick Setup

Dimensions, colors, and (x, y) coordinates are defined for each element to be drawn. Rect is a built in class in pygame that handles shape dimensions useful for collision detection.
</br>
```python
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
```

</br>
The bricks start off as Orange but change color on each hit.
</br></br>
<p align = "center">
  <img src="https://github.com/daimbk/brick-breaker/assets/51926730/f2d52747-9666-41e8-b1ff-b8fcce29eefe" width="798" height
  ="351" border="15"/>
  </br></br>
  <img src="https://github.com/daimbk/brick-breaker/assets/51926730/9b89c27f-3f24-4969-9b87-b3fb1c3c4531" width="798" height
  ="351" border="15"/>
  </br></br>
  <img src="https://github.com/daimbk/brick-breaker/assets/51926730/0eda526e-e57f-4ac0-9650-e95d8f364cfc" width="798" height
  ="351" border="15"/>
</p>

<hr>

## Collision Detection
Collision of the ball with paddle, walls and bricks has been implemented.
</br>
- **Collision with Walls**
  </br>Done using comparison with ball and screen dimension. The ball direction is adjusted accordingly.
```python
if ball_x <= ball_radius or ball_x >= width - ball_radius:
  ball_dx *= -1
if ball_y <= ball_radius:
  ball_dy *= -1
```
</br>

- **Collision with Paddle**
  Done using built-in pygame method to see if Rect objects are colliding.
```python
ball = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)

if ball.colliderect(pygame.Rect(player_x, player_y, player_width, player_height)):
  ball_dy *= -1
```
</br>

- **Collision with Bricks**
  Done using built-in pygame coliderect method to see if Rect objects are colliding. Checked for all present bricks currently not destroyed.
```python
for brick in bricks:
  if ball.colliderect(brick):
      bricks.remove(brick) # destroy brick
      ball_dy *= -1
      # change brick colors on hit (select random rgb values using randint)
      brick_color = (randint(0, 255), randint(0, 255), randint(0, 255))
      score += 1
```

<hr>

## Game Over / Win Screens
Font rendering is used from pygame to display GAME OVER message if ball goes below paddle. WIN is displayed when all bricks are destroyed without failing.
</br></br>
In both screens PLAY AGAIN and QUIT are also displayed which act as buttons to restart the game or exit the game window respectively.

```python
pygame.font.init()
font = pygame.font.SysFont(None, 50)

game_over_text = font.render("GAME OVER", True, RED)
screen.blit(game_over_text, ((width - game_over_text.get_width()) // 2, height // 2))

win_text = font.render("WIN", True, GREEN)
screen.blit(win_text, ((width - game_over_text.get_width()) // 2, height // 2))
```

<p align = "center">
  <img src="https://github.com/daimbk/brick-breaker/assets/51926730/4620db15-ee18-4674-b6fa-1c7d524511db" width="798" height
  ="351" border="15"/>
  </br></br>
  <img src="https://github.com/daimbk/brick-breaker/assets/51926730/00d76623-bed8-4873-ad14-bd0ca540d03f" width="798" height
  ="351" border="15"/>
</p>
