import pytest

from tic_tac_toe import EMPTY, is_draw, new_board, parse_move, render, winner


def board_from(rows: str) -> list[str]:
    """Build a board from 9 characters, using "." for empty: "XO.X....."."""
    return [EMPTY if c == "." else c for c in rows]


def test_new_board_is_empty():
    assert new_board() == [EMPTY] * 9


def test_render_shows_marks_and_free_numbers():
    expected = (
        " X | O | 3\n"
        "---+---+---\n"
        " 4 | X | 6\n"
        "---+---+---\n"
        " 7 | 8 | 9"
    )
    assert render(board_from("XO..X....")) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("1", 0),
        ("9", 8),
        (" 5 ", 4),     # stray spaces are fine
        ("0", None),    # off the board
        ("10", None),
        ("x", None),    # not a number
        ("", None),
        ("2", None),    # taken, see the board below
    ],
)
def test_parse_move(text, expected):
    board = board_from(".O.......")
    assert parse_move(text, board) == expected


@pytest.mark.parametrize(
    "rows, expected",
    [
        ("XXX......", "X"),   # top row
        ("...OOO...", "O"),   # middle row
        ("X..X..X..", "X"),   # left column
        ("..O..O..O", "O"),   # right column
        ("X...X...X", "X"),   # diagonal
        ("..O.O.O..", "O"),   # other diagonal
        ("XO.......", None),  # nobody yet
        ("XOXXOOOXX", None),  # full board, no line
    ],
)
def test_winner(rows, expected):
    assert winner(board_from(rows)) == expected


def test_draw_when_full_and_no_winner():
    assert is_draw(board_from("XOXXOOOXX"))


def test_not_draw_while_squares_are_free():
    assert not is_draw(board_from("XO......."))


def test_not_draw_when_last_move_wins():
    assert not is_draw(board_from("XXXOOXOXO"))
