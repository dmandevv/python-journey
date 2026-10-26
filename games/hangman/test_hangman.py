"""
main() asks for input, so it isn't tested here: play it to check it.
Everything it uses is tested below.
"""
import pytest

from hangman import MAX_WRONG, STAGES, WORDS_FILE, is_solved, load_words, masked, parse_guess, wrong_guesses


# --- load_words --------------------------------------------------------------

def test_load_words_cleans_each_line(tmp_path):
    path = tmp_path / "words.txt"
    path.write_text("apple\n  Banana \n\n cherry\n")
    assert load_words(path) == ["apple", "banana", "cherry"]


def test_the_real_word_list_is_usable():
    words = load_words(WORDS_FILE)
    assert words
    assert all(word.isalpha() and word.islower() for word in words)


def test_there_is_a_drawing_for_every_wrong_guess():
    assert len(STAGES) == MAX_WRONG + 1     # 0 wrong guesses up to MAX_WRONG


# --- masked ------------------------------------------------------------------

@pytest.mark.parametrize(
    "word, guessed, expected",
    [
        ("hangman", set(), "_ _ _ _ _ _ _"),
        ("hangman", {"a", "n"}, "_ a n _ _ a n"),           # every copy of a letter shows
        ("hangman", {"h", "a", "n", "g", "m"}, "h a n g m a n"),
        ("cat", {"x", "z"}, "_ _ _"),                         # wrong letters don't show
        ("a", {"a"}, "a"),
    ],
)
def test_masked(word, guessed, expected):
    assert masked(word, guessed) == expected


# --- wrong_guesses -----------------------------------------------------------

@pytest.mark.parametrize(
    "word, guessed, expected",
    [
        ("hangman", set(), set()),
        ("hangman", {"a", "e", "s"}, {"e", "s"}),
        ("cat", {"c", "a", "t"}, set()),
        ("cat", {"x", "y", "z"}, {"x", "y", "z"}),
    ],
)
def test_wrong_guesses(word, guessed, expected):
    assert wrong_guesses(word, guessed) == expected


# --- is_solved ---------------------------------------------------------------

@pytest.mark.parametrize(
    "word, guessed, expected",
    [
        ("cat", {"c", "a", "t"}, True),
        ("cat", {"c", "a", "t", "x", "y"}, True),       # wrong guesses don't matter
        ("hangman", {"h", "a", "n", "g", "m"}, True),   # a repeated letter is guessed once
        ("cat", {"c", "a"}, False),
        ("cat", set(), False),
    ],
)
def test_is_solved(word, guessed, expected):
    assert is_solved(word, guessed) == expected


# --- parse_guess -------------------------------------------------------------

@pytest.mark.parametrize(
    "text, guessed, expected",
    [
        ("e", set(), "e"),
        ("E", set(), "e"),          # lower case
        (" e ", set(), "e"),        # spaces around it are fine
        ("e", {"e"}, None),         # already guessed
        ("E", {"e"}, None),         # already guessed, in the other case
        ("", set(), None),
        ("   ", set(), None),
        ("ab", set(), None),        # more than one letter
        ("3", set(), None),         # not a letter
        ("?", set(), None),
    ],
)
def test_parse_guess(text, guessed, expected):
    assert parse_guess(text, guessed) == expected
