"""
File: draw_line.py
Name: Ada Wang
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


SIZE = 10
switch = 1
window = GWindow(width=400, height=400, title='draw line')
point = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(event):
    """
    When user clicks on the first time, a circle appears.
    A line appears at the condition where the circle disappears as the user clicks on the canvas for the second time.

    """
    global switch
    if switch == 1:  
        point.x = event.x - SIZE/2
        point.y = event.y - SIZE/2
        point.color = 'black'
        window.add(point)
        switch = 0
    elif switch == 0:
        point.color = 'white'
        line = GLine(point.x + SIZE/2, point.y + SIZE/2, event.x, event.y)
        window.add(line)
        switch = 1
    print('point.x:'+str(point.x))
    print('point.y:'+str(point.y))
    print('event.x:'+str(event.x))
    print('event.y:'+str(event.y))


if __name__ == "__main__":
    main()
