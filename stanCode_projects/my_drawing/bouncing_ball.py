"""
File: bouncing ball.py
Name: Ada Wang
-------------------------

"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 5
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
switch = 1
count = 1
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)


def main():
    global switch
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(ball_move)


def ball_move(m):
    global GRAVITY
    global switch
    global count
    if switch == 1 and count <= 3:
        gravity1 = GRAVITY
        ball.filled = True
        ball.fill_color = 'black'
        window.add(ball)
        switch = 0
        while True:
            if switch == 1:
                break
            ball.move(VX, gravity1)
            gravity1 += GRAVITY
            pause(DELAY)
            if ball.y+ball.height >= window.height:
                gravity1 = -gravity1*REDUCE
            if ball.x+ball.width >= window.width:
                ball.x = START_X
                ball.y = START_Y
                switch = 1
                count += 1
        print('count:' + str(count))  # check count
        print('switch:' + str(switch))  # check switch


if __name__ == "__main__":
    main()
