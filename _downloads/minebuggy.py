from random import randint


def generate_boards():
    """
    A board is a two dimensional 9x9 array
    This function generates a board with 10 bombs located
    at different random positions, a 2D 9x9 array filled with
    empty spaces that will be used to store the state of the game,
    and a list of tuples with the coordinates of the bombs.

    This function is buggy!
    """

    board = [[0 for _ in range(9)] for _ in range(9)]
    opened = [[" " for _ in range(9)] for _ in range(9)]
    bombs = []

    for _ in range(10):
        row = randint(0, 8)
        col = randint(0, 8)
        board[row][col] = -1
        bombs.append([row, col])
        update_neighbors(board, row, col)
    return board, opened, bombs


def update_neighbors(board, row, col):
    """
    Updates the neighbors after adding a bomb to the board
    This function is also buggy.
    """

    for neigh_row in range(max(0, row-1), min(9, row+1)):
        for neigh_col in range(max(0, col-1), min(9, col+1)):
            board[neigh_row][neigh_col] += 1 if board[neigh_row][neigh_col] >= 0 else 0


def print_board(board):
    """
    Prints a board to stdout
    """
    board_size = len(board)
    print("    A   B   C   D   E   F   G   H   I")
    print("  ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗")
    for row in range(board_size-1):
        squares = "║".join(f" {x} " for x in board[row])
        print(f"{row} ║{squares}║")
        print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")

    squares = "║".join(f" {x} " for x in board[-1])
    print(f"{board_size-1} ║{squares}║")
    print("  ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝")


def translate_input(square):
    """
    Converts a string representation of a square to its
    row-column representation
    If the conversion is not possible, the returned values
    are equal to None
    """
    try:
        # column is a letter, so we use
        # the ascii code to translate to a numeric index
        col = ord(square[0].upper()) - 65
        if col > 8 or col < 0:
            return None, None
        row = int(square[1])
        if row > 8 or col < 0:
            return None, None
        return row, col
    except ValueError:
        return None, None


def get_input():
    """
    Obtains user input and returns the corresponding square coordinates
    """
    while True:
        square = input("Please enter a square(e.g. A5):")
        row, col = translate_input(square)
        if row is not None and col is not None:
            return row, col


def open_squares(square_row, square_col, opened, board):
    """
    Opens squares and updates the state of "opened"
    When a square has no neighboring bombs, all of its neighbors are opened.
    Returns the number of opened squares
    This function is also buggy.
    """
    square_update_queue = [(square_row, square_col)]

    opened_count = 0

    while square_update_queue:
        row, col = square_update_queue.pop()
        opened_count += 1
        if opened[row][col] == " ":
            opened[row][col] = str(board[row][col])
            # if the current square has no neighboring bombs
            # add all of its neighbors to the queue
            if board[row][col] == 0:
                for neigh_row in range(max(0, row-1), min(9, row+1)):
                    for neigh_col in range(max(0, col-1), min(9, col+1)):
                        square_update_queue.append((neigh_row, neigh_col))

    return opened_count


def main():
    """
    Main minesweeper function
    """
    board, opened, bombs = generate_boards()
    ended = False
    opened_count = 0
    while not ended:
        print_board(opened)
        row, col = get_input()
        if board[row][col] == -1:
            opened[row][col] = '✷'
            print_board(opened)
            print("You lose!")
            return
        opened_count += open_squares(row, col, opened, board)
        if opened_count == 71:
            for bomb in bombs:
                opened[bomb[0]][bomb[1]] = '✷'
            print_board(opened)
            print("You win!")
            return


if __name__ == '__main__':
    main()
