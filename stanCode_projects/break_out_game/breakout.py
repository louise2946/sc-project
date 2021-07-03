"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program is a Breakout Game. You have 3 lives to play.
If you break out all the bricks, then you win the game, else you lost.

"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel
import random

FRAME_RATE = 1000 / 150  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    get_the_dx = graphics.get_the_dx()
    get_the_dy = graphics.get_the_dy()
    lives = NUM_LIVES
    score_label2 = GLabel(str(lives) + 'LEFT!')
    # Add animation loop here
    while True:
        # update
        # Detect the bricks exists or not. If remove all the bricks, means game clear.
        if graphics.no_more_brick() is False:
            score_label = GLabel('YOU WIN!')
            score_label.font = '-40'
            score_label.color = 'DarkSalmon'
            graphics.window.add(score_label, x=graphics.window.width/2, y=graphics.window.height/2)
            graphics.window.remove(graphics.ball)
            break
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            lives -= 1
            graphics.switch = 0  # click the ball and start a new turn
            if lives > 0:
                # restart the game
                print(lives)
                score_label2.text = str(lives) + ' BALL(S) LEFT!'
                graphics.reset_ball()
                score_label2.font = '-15'
                score_label2.color = 'teal'
                graphics.window.add(score_label2, x=graphics.window.width / 2,
                                    y=graphics.window.height / 2)
                pause(FRAME_RATE)
            else:
                # game over
                score_label1 = GLabel('YOU LOSE!')
                graphics.window.remove(graphics.ball)
                score_label1.font = '-40'
                score_label1.color = 'khaki'
                graphics.window.add(score_label1, x=graphics.window.width/2, y=graphics.paddle_y+graphics.window.height /2)
                break
        if graphics.switch == 1:
            graphics.window.remove(score_label2)
            graphics.ball.move(get_the_dx, get_the_dy)
        # check
        if graphics.touch_brick() or graphics.ball.y <= 0:
            get_the_dy *= -1
        if graphics.touch_paddle() and get_the_dy > 0:
            get_the_dy *= -1
            if random.random() > 0.5:
                get_the_dx *= -1
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            get_the_dx *= -1
        # pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
