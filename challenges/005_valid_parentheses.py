"""
005 - Valid Parentheses

`s` contains only the characters ( ) [ ] { }. Return True if every bracket
is closed by the same type of bracket, in the right order.

    is_valid("()[]{}")  ->  True
    is_valid("([{}])")  ->  True     (nested is fine)
    is_valid("(]")      ->  False    (wrong type)
    is_valid("([)]")    ->  False    (closed in the wrong order)

Run the tests:  .venv/bin/pytest challenges/005_valid_parentheses.py
"""
import pytest

BRACKETS = {")":"(", "}":"{", "]":"["}

def is_valid(s: str) -> bool:
    stack = []
    for b in s.replace(" ", ""):
        if b not in BRACKETS:
            stack.append(b)
            continue
        # Closing bracket matches top of stack
        elif stack and BRACKETS[b] == stack.pop():
            continue
        return False
    return not stack




@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("([{}])", True),
        ("{[]}()", True),
        ("", True),          # nothing open, nothing wrong
        ("(]", False),
        ("([)]", False),
        ("(", False),        # never closed
        (")", False),        # closed before anything opened
        ("(()", False),
        ("())", False),
        ("]]", False),
        ("()  []", True),
        ("  ", True),        # only spaces: replace() leaves "", so nothing is open
    ],
)
def test_is_valid(s, expected):
    assert is_valid(s) == expected
