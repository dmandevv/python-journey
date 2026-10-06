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
        print(f"Invalid row value: '{row}'")
        return None
    row = int(row)
    if row not in range(1, board.size + 1):
        print(f"Row '{row}' not inside board: 1 - {board.size}")
        return None
    if not column.strip().isdigit():
        print(f"Invalid column value: '{column}'")
        return None
    column = int(column)
    if column not in range(1, board.size + 1):
        print(f"Column '{column}' not inside board: 1 - {board.size}")
        return None
    index = (row - 1) * board.size + (column - 1)
    if not board.tiles[index] == TILE.EMPTY:
        print(f"Chosen tile is already: {board.tiles[index].value}")
        return None
    return index


def winner(board: Board) -> TILE | None:
    #check columns
    for col in range(0, board.size):
        if (tile := line_is_winner(board.tiles[col::board.size])): 
            return tile
    #check rows
    for row in range(0, board.size):
        if (tile := line_is_winner(board.tiles[row * board.size:(row + 1) * board.size])):
            return tile
    #check diagonal (top-left to bottom-right)
    if (tile := line_is_winner(board.tiles[0::board.size + 1])):
        return tile
    #check diagonal (top-right to bottom-left)
    if (tile := line_is_winner(board.tiles[board.size - 1:-1:board.size - 1])):
        return tile

def is_full(board: Board) -> bool:
    return all(tile != TILE.EMPTY for tile in board.tiles)

def line_is_winner(line: list[TILE]) -> TILE | None:
    if(all(tile == line[0] for tile in line) and line[0] != TILE.EMPTY):
        return line[0]

def main() -> None:
    first = TILE.X
    while(True):
        first = start_new_game(first)
        while(True):
            again = input(f"Play again? (y/n): ")
            if ("y" in again.lower()):
                break
            elif ("n" in again.lower()):
                print("Goodbye! :-)")
                return

def start_new_game(first_turn: TILE = TILE.X) -> TILE:
    print(f"Starting game...\n\n")
    current_player = first_turn
    board = new_board()

    while(True):
        print(render(board=board))

        while(True):
            row = input(f"Player {current_player.value}, choose a row (1 - {board.size}): ")
            column = input(f"Player {current_player.value}, choose a column (1 - {board.size}): ")
            valid_tile_index = parse_move(row, column, board)
            if valid_tile_index is not None:
                board.tiles[valid_tile_index] = current_player
                break

        if (winning_player := winner(board)):
            print(render(board=board))
            print(f"Winner is '{winning_player.value}'!")
            return TILE.O if winning_player is TILE.X else TILE.X
        
        current_player = TILE.O if current_player is TILE.X else TILE.X
        
        if is_full(board):
            print(render(board=board))
            print("DRAW")
            return current_player



        


if __name__ == "__main__":
    main()
