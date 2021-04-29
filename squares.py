#Student Number: 19019021

import sys
from ezgraphics import GraphicsWindow

WIDTH = 500
BOARD_DIMENSION = 10
SQUARE_DIMENSION = WIDTH / BOARD_DIMENSION
MORTAR_WIDTH = 2
MORTAR_COLOR = "grey"


def draw_cafe_wall(canvas, x, y, square_dimension, board_dimension):
    """
    Draw cafe wall illusion.

    Parameters
    ----------
    canvas : GraphicsCanvas
        A reference to the GraphicsCanvas contained in the window
    x : int
        x coordinate of the top-left corner of the row
    y : int
        y coordinate of the top-left corner of the row
    square_dimension : int
        side length in pixels of a square
    board_dimension : int
        number of squares in one side of the board

    """
    for x in range (BOARD_DIMENSION+1):
        for y in range (BOARD_DIMENSION):
            if(y%2 == 0):
                if(x%2 ==0):
                    canvas.setFill("white")
            else:
                if(x%2 ==1):
                    canvas.setFill("white")
            if(y%2 == 1):
                canvas.setOutline(MORTAR_COLOR)
                canvas.setLineWidth(MORTAR_WIDTH)
                canvas.drawRectangle(x*50, y*50, SQUARE_DIMENSION, SQUARE_DIMENSION)
            else:
                canvas.setOutline(MORTAR_COLOR)
                canvas.setLineWidth(MORTAR_WIDTH)
                #drawing on top of the remaining squares after shifting it 25 pixels back
                canvas.drawRectangle(((x*50)-25), ((y*50)), SQUARE_DIMENSION, SQUARE_DIMENSION)
            canvas.setFill("black")
    pass


def draw_chequerboard(canvas, x, y, square_dimension, board_dimension,
                      chequers=False):
    """
    Draw the board.

    Parameters
    ----------
    canvas : GraphicsCanvas
        A reference to the GraphicsCanvas contained in the window
    x : int
        x coordinate of the top-left corner of the row
    y : int
        y coordinate of the top-left corner of the row
    square_dimension : int
        side length in pixels of a square
    board_dimension : int
        number of squares in a side of the board
    chequers : boolean
        Used to indicate whether the squares in every row should be
        alternately black and white

    """
    if(chequers == False):
        for x in range (BOARD_DIMENSION):
            for y in range (BOARD_DIMENSION):
                if(x%2 == 0):
                    canvas.setFill("white")
                canvas.drawRectangle(x*50, y*50, SQUARE_DIMENSION, SQUARE_DIMENSION)
                canvas.setFill("black")
    elif(chequers == True):
        for x in range (BOARD_DIMENSION):
            for y in range (BOARD_DIMENSION):
                if(y%2 == 0):
                    if(x%2 ==0):
                        canvas.setFill("white")
                else:
                    if(x%2 ==1):
                        canvas.setFill("white")
                canvas.drawRectangle(x*50, y*50, SQUARE_DIMENSION, SQUARE_DIMENSION)
                canvas.setFill("black")
      
    pass


def usage_message():
    """
    Return usage message for this program.


    Returns
    -------
    str
        Usage message

    """

    return 'illusion.py: incorrect usage\n' \
        + 'Use:\n' \
        + '\tillusion.py -chequers or\n' \
        + '\tillusion.py -columns or\n' \
        + '\tillusion.py -cafe or\n' \
        + '\tillusion.py'


def check_args(args):
    """
    Check the arguments passed to the program.


    Parameters
    ----------
    args : list
        List of strings in argv containing the options passed to this program

    Returns
    -------
    boolean
        False if option is invalid, True if option is valid

    """

    # Process the command line input
    valid_option = False
    if len(args) == 1:
        valid_option = args[0] == "-chequers" or args[0] == "-cafe"\
            or args[0] == "-columns"
    elif len(args) == 0:
        valid_option = True

    return valid_option


def main():
    args = sys.argv[1:]

    okay = check_args(args)

    option = "-columns"

    if okay:
        # Create a graphics window (WIDTH x WIDTH pixels):
        win = GraphicsWindow(WIDTH, WIDTH)

        # Access the canvas contained in the graphics window:
        canvas = win.canvas()
        if len(args) == 1:
            option = args[0]

        if option == "-columns":
            draw_chequerboard(canvas, 0, 0, SQUARE_DIMENSION, BOARD_DIMENSION)
        elif option == "-chequers":
            draw_chequerboard(canvas, 0, 0, SQUARE_DIMENSION, BOARD_DIMENSION,
                              chequers=True)
        else:   # args[0] == "-cafe":
            draw_cafe_wall(canvas, 0, 0, SQUARE_DIMENSION, BOARD_DIMENSION)

        # Wait for the user to close the window
        win.wait()
    else:
        print(usage_message())
        exit(1)


if __name__ == "__main__":
    main()
