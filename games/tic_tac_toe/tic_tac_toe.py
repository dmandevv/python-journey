"""
Tic-tac-toe for two players at one keyboard.

Squares are chosen 1-9, laid out like a phone keypad:

     1 | 2 | 3
    ---+---+---
     4 | 5 | 6
    ---+---+---
     7 | 8 | 9

The board is a list of 9 strings: "X", "O", or " " for empty.
Square 1 is board[0], square 9 is board[8].

Play:        .venv/bin/python games/tic_tac_toe/tic_tac_toe.py
Run tests:   .venv/bin/pytest games/tic_tac_toe
"""

from enum import Enum

TILE_SPACING = 1

class TILE(Enum):
    EMPTY = " "
    X = "X"
    O = "O"

class Board:
    def __init__(self, size):
        self.size = size
        self.tiles = [TILE.EMPTY] * (size * size)
    
def new_board() -> Board:
    return Board(3)

def render(board: Board) -> str:
    rendered = ""
    for index, tile in enumerate(board.tiles):
        row = (index + 1) // board.size
        column = (index + 1) % board.size
        rendered += f"{" " * TILE_SPACING}{tile.value}{" " * TILE_SPACING}"
        if not column == 0:
            rendered += "|"
        elif not row == board.size:
            rendered += render_line(board.size)
    return rendered

def render_line(size: int) -> str:
    return f"\n{"-" * ((TILE_SPACING * 2) + 1)}+{"-" * ((TILE_SPACING * 2) + 1)}+{"-" * ((TILE_SPACING * 2) + 1)}\n"

def parse_move(row: str, column: str, board: Board) -> int | None:
    if not row.strip().isdigit():
        return None
    row = int(row)
    if row not in range(1, board.size):
        return None
    if not column.strip().isdigit():
        return None
    column = int(column)
    if column not in range(1, board.size):
        return None
    index = row - 1 + column - 1
    if not board.tiles[index] == TILE.EMPTY:
        return None
    return index


def winner(board: list[str]) -> str | None:
    """Return "X" or "O" if that player has three in a row, otherwise None."""
    pass


def is_draw(board: list[str]) -> bool:
    """Return True if the board is full and nobody has won."""
    pass


def main() -> None:
    while(True):       
        board = new_board()
        print(render(board=board))
        current_player = TILE.X

        while(True):
            row = input(f"Player {current_player.value}, choose a row (1 - {board.size}): ")
            column = input(f"Player {current_player.value}, choose a column (1 - {board.size}): ")
            index = parse_move(row, column, board)
            if index is not None:
                board.tiles[index] = current_player.value

        if current_player is TILE.X:
            current_player = TILE.O
        else:
            current_player = TILE.X

        

        


if __name__ == "__main__":
    main()
