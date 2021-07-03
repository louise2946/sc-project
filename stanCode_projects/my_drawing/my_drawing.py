"""
File: my_drawing.py - Pika Pika
Name: Ada Wang
----------------------

"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLine, GArc, GLabel
from campy.graphics.gwindow import GWindow

window = GWindow(width=555, height=450, title='draw line')


def main():
    """
    This program draws a furry pikachu, healing the days of wfh.
    """
    # lightning
    light = GPolygon()
    size = 505
    t = 355
    light.add_vertex((size+10, size+20-t))
    light.add_vertex((size-15, size+70-t))
    light.add_vertex((size+20, size+80-t))
    light.add_vertex((size+5, size+110-t))
    light.add_vertex((size+30, size+70-t))
    light.add_vertex((size-5, size+60-t))
    light.filled = True
    light.fill_color = 'yellow'
    light.color = 'yellow'
    window.add(light)

    light1 = GPolygon()
    size1 = 509
    t1 = 359
    light1.add_vertex((size1+10, size1+20-t1))
    light1.add_vertex((size1-15, size1+70-t1))
    light1.add_vertex((size1+20, size1+80-t1))
    light1.add_vertex((size1+5, size1+110-t1))
    light1.add_vertex((size1+30, size1+70-t1))
    light1.add_vertex((size1-5, size1+60-t1))
    light1.filled = True
    light1.fill_color = 'grey'
    light1.color = 'grey'
    window.add(light1)


    # text
    text0 = GLabel('ピッカッ', x=377, y=220)
    text0.font = 'Courier-30-bold'
    text0.color = 'yellow'
    window.add(text0)
    text = GLabel('ピッカッ', x=380, y=220)
    text.font = 'Courier-30-bold'
    window.add(text)
    text11 = GLabel('PIKA PIKA', x=388, y=240)
    text11.font = 'Dialog-20-bold'
    text11.color = 'yellow'
    window.add(text11)
    text1 = GLabel('PIKA PIKA', x=390, y=240)
    text1.font = 'Dialog-20-bold'
    window.add(text1)

    text2 = GLabel('Ada Wang @ stanCode', x=370, y=430)
    text2.font = 'Dialog-15-bold'
    text2.color = 'khaki'
    window.add(text2)

    # background
    background = GOval(300, 50, x=80, y=350)
    background.filled = True
    background.fill_color = 'green'
    background.color = 'green'
    window.add(background)
    # pikachu tail
    tail = GPolygon()
    tail.add_vertex((65, 250))
    tail.add_vertex((100, 260))
    tail.add_vertex((90, 290))
    tail.add_vertex((110, 300))
    tail.add_vertex((105, 310))
    tail.add_vertex((130, 320))
    tail.add_vertex((170, 220))
    tail.add_vertex((80, 190))
    tail.filled = True
    tail.fill_color = 'goldenrod'
    tail.color = 'white'
    window.add(tail)

    tail = GPolygon()
    tail.add_vertex((110, 300))
    tail.add_vertex((105, 310))
    tail.add_vertex((130, 320))
    tail.add_vertex((170, 250))
    tail.filled = True
    tail.fill_color = 'DarkGoldenRod'
    tail.color = 'DarkGoldenRod'
    window.add(tail)

    # pokemon ball
    ball = GOval(80, 80, x=200, y=10)
    ball.color = 'grey'
    window.add(ball)
    red_ball = GArc(80, 160, 0, 180)
    red_ball.filled = True
    red_ball.fill_color = 'red'
    red_ball.color = 'red'
    window.add(red_ball, x=200, y=10)
    line = GLine(200, 50, 280, 50)
    line.color = 'grey'
    window.add(line)
    ball2 = GOval(20, 20, x=230, y=40)
    ball2.filled = True
    ball2.fill_color = 'white'
    ball2.color = 'grey'
    window.add(ball2)

    # pikachu ear
    triangle1 = GPolygon()
    triangle1.add_vertex((90, 50))
    triangle1.add_vertex((160, 120))
    triangle1.add_vertex((140, 200))
    triangle1.filled = True
    triangle1.fill_color = 'gold'
    triangle1.color = 'white'
    window.add(triangle1)

    triangle2 = GPolygon()
    triangle2.add_vertex((90, 50))
    triangle2.add_vertex((120, 80))
    triangle2.add_vertex((110, 110))
    triangle2.filled = True
    triangle2.fill_color = 'black'
    triangle2.color = 'black'
    window.add(triangle2)

    triangle3 = GPolygon()
    triangle3.add_vertex((370, 50))
    triangle3.add_vertex((300, 120))
    triangle3.add_vertex((320, 200))
    triangle3.filled = True
    triangle3.fill_color = 'gold'
    triangle3.color = 'white'
    window.add(triangle3)

    triangle4 = GPolygon()
    triangle4.add_vertex((370, 50))
    triangle4.add_vertex((340, 80))
    triangle4.add_vertex((350, 110))
    triangle4.filled = True
    triangle4.fill_color = 'black'
    triangle4.color = 'black'
    window.add(triangle4)

    # pikachu leg
    yellow_ball3 = GOval(20, 30)
    yellow_ball3.filled = True
    yellow_ball3.fill_color = 'goldenrod'
    yellow_ball3.color = 'goldenrod'
    window.add(yellow_ball3, x=150, y=355)

    yellow_ball4 = GOval(20, 30)
    yellow_ball4.filled = True
    yellow_ball4.fill_color = 'goldenrod'
    yellow_ball4.color = 'goldenrod'
    window.add(yellow_ball4, x=300, y=355)


    # pikachu body
    yellow_ball = GArc(250, 520, 0, 180)
    yellow_ball.filled = True
    yellow_ball.fill_color = 'gold'
    yellow_ball.color = 'gold'
    window.add(yellow_ball, x=110, y=91)

    yellow_ball1 = GPolygon()
    yellow_ball1.add_vertex((110, 220))
    yellow_ball1.add_vertex((130, 350))
    yellow_ball1.add_vertex((350, 348))
    yellow_ball1.add_vertex((360, 220))
    yellow_ball1.filled = True
    yellow_ball1.fill_color = 'gold'
    yellow_ball1.color = 'gold'
    window.add(yellow_ball1)

    yellow_ball2 = GOval(221, 50)
    yellow_ball2.filled = True
    yellow_ball2.fill_color = 'gold'
    yellow_ball2.color = 'gold'
    window.add(yellow_ball2, x=129, y=320)

    yellow_ball5 = GOval(20, 40)
    yellow_ball5.filled = True
    yellow_ball5.fill_color = 'goldenrod'
    yellow_ball5.color = 'goldenrod'
    window.add(yellow_ball5, x=150, y=255)

    yellow_ball6 = GOval(40, 20)
    yellow_ball6.filled = True
    yellow_ball6.fill_color = 'goldenrod'
    yellow_ball6.color = 'goldenrod'
    window.add(yellow_ball6, x=350, y=235)

    # pikachu eyes
    eye_ball_l = GOval(20, 20)
    eye_ball_l.filled = True
    eye_ball_l.fill_color = 'black'
    window.add(eye_ball_l, x=195, y=160)
    eye_ball_r = GOval(20, 20)
    eye_ball_r.filled = True
    eye_ball_r.fill_color = 'black'
    window.add(eye_ball_r, x=275, y=160)
    eye_ball_l1 = GOval(7, 7)
    eye_ball_l1.filled = True
    eye_ball_l1.fill_color = 'white'
    eye_ball_l1.color = 'white'
    window.add(eye_ball_l1, x=205, y=162)
    eye_ball_r1 = GOval(7, 7)
    eye_ball_r1.filled = True
    eye_ball_r1.fill_color = 'white'
    eye_ball_r1.color = 'white'
    window.add(eye_ball_r1, x=280, y=162)

    # pikachu mouth
    mouth = GOval(9, 7, x=240, y=180)
    mouth.filled = True
    mouth.color = 'black'
    mouth.fill_color = 'black'
    window.add(mouth)

    mouth1 = GOval(20, 20, x=224, y=188)
    mouth1.color = 'black'
    window.add(mouth1)

    mouth2 = GOval(20, 20, x=244, y=188)
    mouth2.color = 'black'
    window.add(mouth2)

    mouth3 = GRect(40, 8, x=224, y=188)
    mouth3.filled = True
    mouth3.fill_color = 'gold'
    mouth3.color = 'gold'
    window.add(mouth3)

    mouth4 = GOval(20, 21, x=150, y=180)
    mouth4.filled = True
    mouth4.fill_color = 'crimson'
    mouth4.color = 'crimson'
    window.add(mouth4)

    mouth5 = GOval(21, 20, x=310, y=180)
    mouth5.filled = True
    mouth5.fill_color = 'crimson'
    mouth5.color = 'crimson'
    window.add(mouth5)

    mouth5 = GOval(18, 7, x=235, y=245)
    mouth5.filled = True
    mouth5.fill_color = 'goldenrod'
    mouth5.color = 'goldenrod'
    window.add(mouth5)

if __name__ == '__main__':
    main()
