![welcome screen](./bg.png)

# Brick Breaker

Classic break-breaker game clone made using pygame utilities. The program uses simple shape drawing methods and collision detection using screen dimensions and collision methods.
</br>

Default screen resolution is 1280x720.

<hr>

## Score System
Each ball hit on brick increments the score by 1. High Score record is kept by saving and loading the high score in a file "high_score.txt".

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

</br>

- **Collision with Paddle**
  Done using built-in pygame method to see if Rect objects are colliding.

</br>

- **Collision with Bricks**
  Done using built-in pygame coliderect method to see if Rect objects are colliding. Checked for all present bricks currently not destroyed.

<hr>

## Game Over / Win Screens
Font rendering is used from pygame to display GAME OVER message if ball goes below paddle. WIN is displayed when all bricks are destroyed without failing.
</br></br>
In both screens PLAY AGAIN and QUIT are also displayed which act as buttons to restart the game or exit the game window respectively.

<p align = "center">
  <img src="https://github.com/daimbk/brick-breaker/assets/51926730/4620db15-ee18-4674-b6fa-1c7d524511db" width="798" height
  ="351" border="15"/>
  </br></br>
  <img src="https://github.com/daimbk/brick-breaker/assets/51926730/00d76623-bed8-4873-ad14-bd0ca540d03f" width="798" height
  ="351" border="15"/>
</p>
