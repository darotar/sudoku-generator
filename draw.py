from turtle import Turtle, tracer

from constant import CELL_SIZE, START_POINT_X, START_POINT_Y, PADDING_X, PADDING_Y, FONT_SIZE


pen = Turtle()
tracer(0)
pen.speed(0)
pen.color('#000000')
pen.hideturtle()


def text(message, x, y, size):
    font = ('Arial', size, 'normal')

    pen.up()
    pen.goto(x, y)
    pen.write(message, align='left', font=font)


def get_pensize(index):
    if (index % 3) == 0:
        return 3
    else:
        return 1


def draw_rows(step):
    pen.up()
    pen.goto(START_POINT_X, START_POINT_Y - step * CELL_SIZE)
    pen.down()
    pen.goto(START_POINT_X + 9 * CELL_SIZE, START_POINT_Y - step * CELL_SIZE)


def draw_cols(step):
    pen.up()
    pen.goto(START_POINT_X + step * CELL_SIZE, START_POINT_Y)
    pen.down()
    pen.goto(START_POINT_X + step * CELL_SIZE, START_POINT_Y - 9 * CELL_SIZE)


def draw_text(board):
    for row in range(0, 9):
        for col in range(0, 9):
            if board[row][col] != 0:
                text(
                    board[row][col],
                    START_POINT_X + col * CELL_SIZE + PADDING_X,
                    START_POINT_Y - row * CELL_SIZE - CELL_SIZE + PADDING_Y,
                    FONT_SIZE
                )


def draw_board(board):
    for step in range(0, 10):
        pen.pensize(get_pensize(step))

        draw_rows(step)
        draw_cols(step)

    draw_text(board)

