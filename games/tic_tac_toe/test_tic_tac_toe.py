import math

import pytest

from tic_tac_toe import TILE, Board, is_full, new_board, parse_move, render, winner


def board_from(rows: str) -> Board:
    """Build a board from a string of tiles, using "." for empty: "XO..X....".
    The length sets the size: 9 characters make a 3x3 board, 16 a 4x4."""
    size = math.isqrt(len(rows))
    board = Board(size)
    board.tiles = [TILE.EMPTY if c == "." else TILE(c) for c in rows]
    return board


def test_new_board_is_empty_3x3():
    board = new_board()
    assert board.size == 3
    assert board.tiles == [TILE.EMPTY] * 9


def test_render():
    expected = (
        " X | O |   \n"
        "---+---+---\n"
        "   | X |   \n"
        "---+---+---\n"
        "   |   |   "
    )
    assert render(board_from("XO..X....")) == expected


@pytest.mark.parametrize(
    "row, column, expected",
    [
        ("1", "1", 0),      # top left
        ("1", "3", 2),      # top right
        ("2", "1", 3),      # first square of the second row
        ("3", "3", 8),      # bottom right
        (" 2 ", "2", 4),    # stray spaces are fine
        ("0", "1", None),   # off the board
        ("4", "1", None),
        ("1", "4", None),
        ("x", "1", None),   # not a number
        ("1", "", None),
        ("1", "2", None),   # taken, see the board below
    ],
)
def test_parse_move(row, column, expected):
    board = board_from(".O.......")
    assert parse_move(row, column, board) == expected


def test_parse_move_uses_the_board_size():
    board = board_from("." * 16)                 # 4x4
    assert parse_move("2", "1", board) == 4      # a row is 4 squares long here
    assert parse_move("4", "4", board) == 15


@pytest.mark.parametrize(
    "rows, expected",
    [
        ("XXX......", TILE.X),   # top row
        ("...OOO...", TILE.O),   # middle row
        ("X..X..X..", TILE.X),   # left column
        ("..O..O..O", TILE.O),   # right column
        ("X...X...X", TILE.X),   # diagonal
        ("..O.O.O..", TILE.O),   # other diagonal
        ("XO.......", None),     # nobody yet
        ("XOXXOOOXX", None),     # full board, no line
    ],
)
def test_winner(rows, expected):
    assert winner(board_from(rows)) == expected


@pytest.mark.parametrize(
    "rows, expected",
    [
        ("XOXXOOOXX", True),    # full, no winner: a draw
        ("XXXOOXOXO", True),    # full, X won: still full, the caller checks winner() first
        ("XO.......", False),
        (".........", False),
        ("XOXXOOOX.", False),   # one square left
    ],
)
def test_is_full(rows, expected):
    assert is_full(board_from(rows)) == expected
