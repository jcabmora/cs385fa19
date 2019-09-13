import random

SIZE = 4
TILE_HEIGHT = 5
TILE_WIDTH = 8
BOARD_WIDTH = SIZE * TILE_WIDTH
BOARD_HEIGHT = SIZE * TILE_HEIGHT


def initialize_board():
    """
    Initializes a board with two randomly added tiles
    A board is a 2D array of SIZE x SIZE.
    Each element on the 2D array will correspond to a tile in the game
    A value of 0 indicates an empty tile
    """
    pass 

def add_random_tile(board):
    """
    Takes a board and randomly adds a new tile
    with a value of 2 or 4 with the former with a probability of 90%
    """
    pass


def get_empty_cells(board):
    """
    Returns a list of empty tiles.
    Tiles should be represented in the form of 2-tuple with its
    board coordinates in the form (row, column)
    e.g. A board with this configuration:

          c0  c1  c2  c3
         ╔═══╦═══╦═══╦═══╗
      r0 ║ 2 ║ 2 ║   ║   ║
         ╠═══╬═══╬═══╬═══╣
      r1 ║   ║ 4 ║ 2 ║ 2 ║
         ╠═══╬═══╬═══╬═══╣
      r2 ║16 ║   ║ 8 ║ 2 ║
         ╠═══╬═══╬═══╬═══╣
      r3 ║32 ║   ║512║   ║
         ╚═══╩═══╩═══╩═══╝


    should return a list:

    [(0, 2), (0, 3), (1, 0), (2, 1), (3, 1), (3, 3)]

    Tiles are not expected to be sorted
    """
    pass


def move_up(board):
    """
    Applies a move in the up direction to all the tiles in a board.
    This function should apply the move directly to the passed board.
    This function returns a boolean that indicates if tiles were moved (or not)

    As an example, the following board will return False since no tiles can be moved in an
    upward direction:

           c0  c1  c2  c3
         ╔═══╦═══╦═══╦═══╗
      r0 ║ 2 ║ 2 ║   ║   ║
         ╠═══╬═══╬═══╬═══╣
      r1 ║ 8 ║ 4 ║   ║   ║
         ╠═══╬═══╬═══╬═══╣
      r2 ║   ║   ║   ║   ║
         ╠═══╬═══╬═══╬═══╣
      r3 ║   ║   ║   ║   ║
         ╚═══╩═══╩═══╩═══╝

    """
    pass


def find_next_position_up(board, row, col):
    """
    Support function that takes a board, and a tile coordinates,
    and returns the position where it should be located after moving upward
    """
    pass


def move_down(board):
    """
    Applies a move in the down direction to all the tiles in a board.
    This function should apply the move directly to the passed board.
    This function returns a boolean that indicates if tiles were moved (or not)
    """
    pass


def find_next_position_down(board, row, col):
    """
    Support function that takes a board, and a tile coordinates,
    and returns the position where it should be located after moving downward
    """
    pass


def move_left(board):
    """
    Applies a move in the left direction to all the tiles in a board.
    This function should apply the move directly to the passed board.
    This function returns a boolean that indicates if tiles were moved (or not)
    """
    pass


def find_next_position_left(board, row, col):
    """
    Support function that takes a board, and a tile coordinates,
    and returns the position where it should be located after moving leftward
    """
    pass


def move_right(board):
    """
    Applies a move in the right direction to all the tiles in a board.
    This function should apply the move directly to the passed board.
    This function returns a boolean that indicates if tiles were moved (or not)
    """
    pass


def find_next_position_right(board, row, col):
    """
    Takes a board, and a tile coordinates,
    and returns the position where it should be located after moving rightward.
    """
    pass


def is_game_over(board):
    """
    Returns a tuple with three elements:

    a boolean that indicates that the game is over if True
    a boolean that indicates taht the game has been won if True
    a score that consists of the sum of all the cells
    """
    pass


def is_tile_movable(board, row, col):
    """
    Determines if a tile can be moved due to the presence of adjacent spaces
    of neighbors with the same value
    This function assumes that is called in a sequence that goes from left to
    right and then from up to down, so it only needs to check on the right and down neighbors.
    """
    pass
