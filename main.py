import pygame as pg

from settings import *
from paddle import Paddle
from ball import Ball
from bricks import Bricks

# Initialize pygame
pg.init()

screen = pg.display.set_mode((WIDTH , HEIGTH))
pg.display.set_caption("Breakout Game")

#Objects
pad = Paddle(paddle_x, paddle_y)
ball = Ball(ball_x, ball_y, screen)
bricks = Bricks(screen, brick_width, brick_height)
clock = pg.time.Clock()

running = True
while running:
    screen.fill(BG_COLOR)

    # Check for quit game
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pad.appear(screen)

    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        pad.move_right()

    if keys[pg.K_LEFT]:
        pad.move_left()

    ball.move()

    ball.check_for_contact_on_x()

    ball.check_for_contact_on_y()

    if (pad.rect.y < ball.y + ball.radius < pad.rect.y + pad.height and
        pad.rect.x < ball.x + ball.radius < pad.rect.x + pad.width):
        ball.bounce_y()
        ball.y = pad.y - ball.radius

    bricks.show_bricks()

    pg.display.flip()

    clock.tick(60)