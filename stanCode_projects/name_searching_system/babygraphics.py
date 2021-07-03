"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    interval = (width - (GRAPH_MARGIN_SIZE*2))/len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + (year_index*interval)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill='grey')
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill='grey')
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT, width=LINE_WIDTH, fill='grey')
    for year_index in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, year_index), 0, get_x_coordinate(CANVAS_WIDTH, year_index), CANVAS_HEIGHT,
                           width=LINE_WIDTH, fill='grey')
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year_index)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text= YEARS[year_index], anchor=tkinter.NW, fill='black', font="times40")


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    color = -1
    for name in range(len(lookup_names)):
        names = lookup_names[name]
        year_rank = []
        name_draw = []
        value = name_data[names]
        if color < 3:
            color += 1
        else:
            color = 0
        for year in YEARS:
            if str(year) in name_data[names]:
                year_rank.append(int(value[str(year)])/MAX_RANK*(CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2))
                name_draw.append(str(names)+' '+str(value[str(year)]))
            else:
                year_rank.append(CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)
                name_draw.append(str(names)+' '+str('*'))
        for i in range(len(year_rank)):
            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, GRAPH_MARGIN_SIZE+year_rank[i],
                               text=name_draw[i], anchor=tkinter.SW, fill=COLORS[color], font="times40")
            if i <= len(year_rank)-2:
                canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), GRAPH_MARGIN_SIZE+year_rank[i],
                                   get_x_coordinate(CANVAS_WIDTH, i+1), GRAPH_MARGIN_SIZE+year_rank[i+1],
                                   width=LINE_WIDTH, fill=COLORS[color])


        print(color)





# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
