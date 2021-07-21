from draw import *
from random import randint, sample


attempts: int = 5
counter: int = 1
number_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def generate_board():
    _board: list[list[int]] = []

    for i in range(0, 9):
        _board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

    return _board


board = generate_board()


def check_board(board_ref: list[list[int]]):
    for row in range(0, 9):
        for col in range(0, 9):
            if board_ref[row][col] == 0:
                return False

    return True


def get_range(axe: int, arr: list[int]):
    return next(filter(lambda item: axe < item, arr))


def get_square(board_ref: list[list[int]], row: int, col: int) -> list[int]:
    square: list[int] = []
    square_combinations: list[int] = [3, 6, 9]

    row_range = get_range(row, square_combinations)
    col_range = get_range(col, square_combinations)

    for i in range(row_range - 3, row_range):
        for j in range(col_range - 3, col_range):
            square.append(board_ref[i][j])

    return square


def is_value_in_column(board_ref: list[list[int]], value: int, col: int) -> bool:
    is_value_in_col: bool = False

    for row in range(0, 9):
        if board_ref[row][col] == value:
            is_value_in_col = True

    return is_value_in_col


def fill_board(board_ref: list[list[int]], is_solving: bool):
    global counter

    row = None
    col = None

    for i in range(0, 81):
        row = i // 9
        col = i % 9

        if board_ref[row][col] == 0:
            shuffled_list = number_list if is_solving else sample(number_list, k=len(number_list))

            for value in shuffled_list:
                if value not in board_ref[row]:
                    if not is_value_in_column(board_ref, value, col):
                        square = get_square(board_ref, row, col)

                        if value not in square:
                            board_ref[row][col] = value

                            if check_board(board_ref):
                                if is_solving:
                                    counter += 1
                                    break
                                else:
                                    return True
                            else:
                                if fill_board(board_ref, is_solving):
                                    return True
            break

    if row is not None and col is not None:
        board_ref[row][col] = 0


if __name__ == "__main__":
    fill_board(board, False)

    while attempts > 0:
        rand_row = randint(0, 8)
        rand_col = randint(0, 8)

        while board[rand_row][rand_col] == 0:
            rand_row = randint(0, 8)
            rand_col = randint(0, 8)

        backup = board[rand_row][rand_col]
        board[rand_row][rand_col] = 0
        copy_board = []

        for r in range(0, 9):
            copy_board.append([])

            for c in range(0, 9):
                copy_board[r].append(board[r][c])

        counter = 0

        fill_board(copy_board, True)

        if counter != 1:
            board[rand_row][rand_col] = backup
            attempts -= 1

        pen.clear()
        pen.getscreen().update()

    draw_board(board)
    input()
