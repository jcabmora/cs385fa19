import random

SIZE = 4
TILE_HEIGHT = 5
TILE_WIDTH = 8
BOARD_WIDTH = SIZE * TILE_WIDTH
BOARD_HEIGHT = SIZE * TILE_HEIGHT


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
    value = 2 if random.random() <= 0.9 else 4
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

