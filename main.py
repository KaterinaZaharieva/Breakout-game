import pygame as pg

from settings import *
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from score import ScoreBoard

# Initialize pygame
pg.init()

screen = pg.display.set_mode((WIDTH , HEIGTH))
pg.display.set_caption("Breakout Game")
clock = pg.time.Clock()

#Objects
pad = Paddle(paddle_x, paddle_y)
ball = Ball(ball_x, ball_y, screen)
bricks = Bricks(screen, brick_width, brick_height)
score = ScoreBoard(text_x, color, screen)
score.set_high_score()


running = True
while running:
    screen.fill(BG_COLOR)
    score.show_score()

    pad.appear(screen)

    bricks.show_bricks()

    # Check for quit game
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Check if there are more trials
    if score.is_game_over():
        score.game_over()

    # Check if all bricks are broken
    elif len(bricks.bricks) == 0:
        score.success()
    else:
        ball.move()


    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        pad.move_right()

    if keys[pg.K_LEFT]:
        pad.move_left()


    ball.check_for_contact_on_x()

    ball.check_for_contact_on_y()

    if (pad.rect.y < ball.y + ball.radius < pad.rect.y + pad.height and
        pad.rect.x < ball.x + ball.radius < pad.rect.x + pad.width):
        ball.bounce_y()
        ball.y = pad.y - ball.radius


    # Check if the ball hits the brick
    for brick in bricks.bricks:
        if brick.collidepoint(ball.x, ball.y - ball.radius) or brick.collidepoint(ball.x, ball.y + ball.radius):
            bricks.bricks.remove(brick)
            ball.bounce_y()
            # Increase score by 1
            score.score += 1

    # Check if ball falls off
    if ball.y + ball.radius >= 580:
        ball.y = pad.y - ball.radius
        pg.time.delay(2000)
        score.trials -= 1
        ball.bounce_y()

    # Restard the game
    if keys[pg.K_0]:
        if score.is_game_over():
            score.score = 0
            score.trials = 5
            bricks.bricks.clear()
            bricks.set_values()


    pg.display.flip()

    clock.tick(60)