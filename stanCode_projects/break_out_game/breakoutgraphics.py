"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random


BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle_y = paddle_offset
        self.paddle_h = paddle_height
        onmousemoved(self.paddle_move)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2, x=self.window.width / 2, y=self.window.height / 2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.ball_2r = ball_radius*2

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        # Draw bricks
        self.brick_w = brick_width  # save brick width
        self.brick_h = brick_height  # save brick height
        self.brick_r = brick_rows  # save brick rows
        self.brick_c = brick_cols  # save brick cols
        self.brick_space = brick_spacing  # save brick_space
        self.brick_row_length = window_width  # save the window width
        self.brick_offset = brick_offset  # Vertical offset of the topmost brick from the window top (in pixels)
        self.brick_column_length = brick_rows * (brick_height + brick_spacing) + self.brick_offset

        # Build the Bricks
        self.build_the_brick()

        # Set ball velocity
        self.set_ball_velocity()

        # Let ball move after click
        self.switch = 0
        onmouseclicked(self.get_switch_on)
        self.window.add(self.ball)
        self.is_brick = False

    def get_switch_on(self, m):
        if self.switch == 0:
            self.switch = 1
        # print(str(self.switch))

    def reset_ball(self):
        self.set_ball_velocity()
        self.ball.x = self.window.width / 2
        self.ball.y = self.window.height / 2
        self.window.add(self.ball)

    # Detect the bricks exists or not. If remove all the bricks, means game clear.
    def no_more_brick(self):
        self.is_brick = False
        for i in range(0, self.brick_row_length, self.brick_w+self.brick_space):
            for j in range(self.brick_offset, self.brick_column_length, self.brick_h+self.brick_space):
                # print('i', str(i),'j',str(j))
                obj = self.window.get_object_at(i, j)
                # print('obj:' ,obj)
                if obj is not None:
                    self.is_brick = True
        return self.is_brick

    def touch_paddle(self):
        # check paddle
        obj1 = self.window.get_object_at(self.ball.x, self.ball.y)
        obj2 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball_2r)
        obj3 = self.window.get_object_at(self.ball.x + self.ball_2r, self.ball.y)
        obj4 = self.window.get_object_at(self.ball.x + self.ball_2r, self.ball.y + self.ball_2r)
        check = (self.window.height - self.paddle_y - self.paddle_h)
        if obj1 == self.paddle or obj2 == self.paddle or obj3 == self.paddle or obj4 == self.paddle:
            touch_paddle = True
        else:
            touch_paddle = False
        return touch_paddle

    def touch_brick(self):
        # check brick
        obj1 = self.window.get_object_at(self.ball.x, self.ball.y)
        obj2 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball_2r)
        obj3 = self.window.get_object_at(self.ball.x + self.ball_2r, self.ball.y)
        obj4 = self.window.get_object_at(self.ball.x + self.ball_2r, self.ball.y + self.ball_2r)
        check = self.brick_column_length
        if self.ball.y > check:
            touch_brick = False
        elif self.ball.y <= check and obj1 is not None:
            touch_brick = True
            self.window.remove(obj1)
        elif self.ball.y <= check and obj2 is not None:
            touch_brick = True
            self.window.remove(obj2)
        elif self.ball.y <= check and obj3 is not None:
            touch_brick = True
            self.window.remove(obj3)
        elif self.ball.y <= check and obj4 is not None:
            touch_brick = True
            self.window.remove(obj4)
        else:
            touch_brick = False
        return touch_brick

    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def get_the_dx(self):
        return self.__dx

    def get_the_dy(self):
        return self.__dy

    def paddle_move(self, event):
        if event.x - self.paddle.width <= 0:
            self.paddle.x = 0
        elif event.x + self.paddle.width >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = event.x - self.paddle.width/2
        self.paddle.y = self.window.height - self.paddle_y
        self.paddle.filled = True
        self.paddle.fill_color = 'gray'
        self.paddle.color = 'white'
        self.window.add(self.paddle)

    def build_the_brick(self):
        for i in range(0, self.brick_row_length, self.brick_w+self.brick_space):
            for j in range(self.brick_offset, self.brick_column_length, self.brick_h+self.brick_space):
                rect = GRect(self.brick_w, self.brick_h)
                self.window.add(rect, i, j)
                rect.filled = True
                rect.fill_color = self.color_change(j)
                rect.color = 'white'

    def color_change(self, num):
        num = random.choice(range(6))
        if num == 0:
            color = 'DarkSalmon'
        elif num == 1:
            color = 'brown'
        elif num == 2:
            color = 'coral'
        elif num == 3:
            color = 'firebrick'
        elif num == 4:
            color = 'pink'
        elif num == 5:
            color = 'IndianRed'
        else:
            color = 'HotPink'
        return color

