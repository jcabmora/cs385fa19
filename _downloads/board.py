import time
import curses
from curses import wrapper

import random


SIZE = 4
TILE_HEIGHT = 5
TILE_WIDTH = 8
BOARD_WIDTH = SIZE * TILE_WIDTH
BOARD_HEIGHT = SIZE * TILE_HEIGHT

COLOR_PAIRS = {
    0: 0,
    2: 1,
    4: 2,
    8: 3,
    16: 4,
    32: 5,
    64: 6,
    128: 6,
    256: 6,
    512: 7,
    1024: 7,
    2048: 7,
}

BORDER_COLOR_PAIRS = {
    0: 0,
    2: 11,
    4: 12,
    8: 13,
    16: 14,
    32: 15,
    64: 16,
    128: 16,
    256: 16,
    512: 17,
    1024: 17,
    2048: 17,
}


def init_curses():
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
    curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_RED)

    curses.init_pair(11, curses.COLOR_WHITE, curses.COLOR_WHITE)
    curses.init_pair(12, curses.COLOR_WHITE, curses.COLOR_YELLOW)
    curses.init_pair(13, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(14, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(15, curses.COLOR_WHITE, curses.COLOR_CYAN)
    curses.init_pair(16, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
    curses.init_pair(17, curses.COLOR_WHITE, curses.COLOR_RED)

def initialize_board():
    """
    Initializes a board with two randomly added tiles
    """

    board = [ [0 for _ in range(SIZE)] for _ in range(SIZE)]
    add_random_tile(board)
    add_random_tile(board)
    return board


def add_random_tile(board):
    """
    Takes a board and randomly adds a new tile 
    with a value of 2 or 4 with the former with a probability of 80%
    """
    empty_spots = get_empty_cells(board)
    new_tile = random.choice(empty_spots)
    value = 2 if random.random() <= 0.8 else 4
    board[new_tile[0]][new_tile[1]] = value


def get_empty_cells(board):
    """
    Returns a list of coordinates of the empty cells
    """
    result = []
    for row in range(SIZE):
        for column in range(SIZE):
            if board[row][column] == 0:
                result.append((row,column))
    return result


def move_up(board):
    moved_tiles = False
    for col in range(SIZE):
        merged = False
        # traverse from the top to the bottom
        # we can skip the first row, since that won't move
        for row in range(1,SIZE):
            if board[row][col] != 0:
                next_row = find_next_position_up(board, row, col)
                if next_row > 0 and board[next_row-1][col] == board[row][col] and not merged:
                    board[next_row-1][col] *= 2
                    board[row][col] = 0
                    moved_tiles = True
                    merged = True
                elif next_row != row:
                    board[next_row][col] = board[row][col]
                    board[row][col] = 0
                    moved_tiles = True
                    merged = False
                else:
                    merged = True
    return moved_tiles


def find_next_position_up(board, row, col):
    curr_row = row
    next_row = row - 1
    while next_row >= 0 and board[next_row][col] == 0:
        curr_row = next_row
        next_row -= 1
    return curr_row

        
def move_down(board):
    moved_tiles = False
    for col in range(SIZE):
        merged = False
        # traverse from the bottom to the top
        # we can skip the first row, since that won't move
        for row in reversed(range(SIZE-1)):
            if board[row][col] != 0:
                next_row = find_next_position_down(board, row, col)
                if next_row < SIZE-1 and board[next_row+1][col] == board[row][col] and not merged:
                    board[next_row+1][col] *= 2
                    board[row][col] = 0
                    moved_tiles = True
                    merged = True
                elif next_row != row:
                    board[next_row][col] = board[row][col]
                    board[row][col] = 0
                    moved_tiles = True
                    merged = False
                else:
                    merged = False
    return moved_tiles


def find_next_position_down(board, row, col):
    curr_row = row
    next_row = row + 1
    while next_row < SIZE and board[next_row][col] == 0:
        curr_row = next_row
        next_row += 1
    return curr_row


def move_left(board):
    moved_tiles = False
    for row in range(SIZE):
        merged = False
        # traverse from the left to the right
        # we can skip the leftmost column, since that won't move
        for col in range(1,SIZE):
            if board[row][col] != 0:
                next_col = find_next_position_left(board, row, col)
                if next_col > 0 and board[row][next_col-1] == board[row][col] and not merged:
                    board[row][next_col-1] *= 2
                    board[row][col] = 0
                    merged = True
                    moved_tiles = True
                elif next_col != col:
                    board[row][next_col] = board[row][col]
                    board[row][col] = 0
                    moved_tiles = True
                    merged = False
                else:
                    merged = False
    return moved_tiles


def find_next_position_left(board, row, col):
    curr_col = col
    next_col = col - 1
    while next_col >= 0 and board[row][next_col] == 0:
        curr_col = next_col
        next_col -= 1
    return curr_col


def move_right(board):
    moved_tiles = True
    for row in range(SIZE):
        merged = False
        # traverse from right to left
        # we can skip the rightmost column, since that won't move
        for col in reversed(range(SIZE-1)):
            if board[row][col] != 0:
                next_col = find_next_position_right(board, row, col)
                if next_col < SIZE-1 and board[row][next_col+1] == board[row][col] and not merged:
                    board[row][next_col+1] *= 2
                    board[row][col] = 0
                    merged = True
                    moved_tiles = True
                elif next_col != col:
                    board[row][next_col] = board[row][col]
                    board[row][col] = 0
                    moved_tiles = True
                    merged = False
                else:
                    merged = False
    return moved_tiles


def find_next_position_right(board, row, col):
    curr_col = col
    next_col = col + 1
    while next_col < SIZE and board[row][next_col] == 0:
        curr_col = next_col
        next_col += 1
    return curr_col


def paint_board(screen, board, offset_y, offset_x):

    y_position = offset_y

    for row in range(SIZE):
        x_position = offset_x 
        for column in range(SIZE):
            paint_tile(screen, board[row][column], y_position, x_position)
            x_position += TILE_WIDTH
        y_position += TILE_HEIGHT

def paint_tile(screen, value, y, x):

    color = COLOR_PAIRS[value]
    border_color = BORDER_COLOR_PAIRS[value] 

    screen.addstr(y, x,"▛▀▀▀▀▀▀▜", curses.color_pair(border_color))
    screen.addstr(y + 1, x, "▌      ▐", curses.color_pair(border_color))
    if value > 0:
        screen.addstr(y + 2, x, "▌", curses.color_pair(border_color))
        screen.addstr(y + 2, x + 1, "{:^6}".format(str(value)), curses.color_pair(color))
        screen.addstr(y + 2, x + 7, "▐".format(str(value)), curses.color_pair(border_color))
    else:
        screen.addstr(y + 2, x, "▌      ▐", curses.color_pair(border_color))
    screen.addstr(y + 3, x, "▌      ▐", curses.color_pair(border_color))
    screen.addstr(y + 4, x, "▙▄▄▄▄▄▄▟", curses.color_pair(border_color))
    screen.refresh()


def main(stdscr):

    init_curses()

    # centering
    height, width = stdscr.getmaxyx()

    offset_x = int((width // 2) - int(BOARD_WIDTH/2))
    offset_y = int((height // 2) - int(BOARD_HEIGHT/2))
    #screen = stdscr.subwin(BOARD_HEIGHT, BOARD_WIDTH, start_y, start_x)
    #screen.box()

    board = initialize_board()
    paint_board(stdscr, board, offset_y, offset_x)

    last_move = None

    while True:
        c = stdscr.getch()
        moved_tiles = False
        
        if c == curses.KEY_UP:
            moved_tiles = move_up(board)
        elif c == curses.KEY_DOWN:
            moved_tiles = move_down(board)
        elif c == curses.KEY_LEFT:
            moved_tiles = move_left(board)
        elif c == curses.KEY_RIGHT:
            moved_tiles = move_right(board)
        elif c == ord('q'):
            stdscr.clear()
            stdscr.addstr("Do you want to exit (press 'y' to confirm)?")
            if stdscr.getch() == ord('y'):
                break

        if moved_tiles:
            add_random_tile(board)
            paint_board(stdscr, board, offset_y, offset_x)

if __name__ == '__main__':
    wrapper(main)
