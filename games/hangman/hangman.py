"""
Hangman in the terminal.

The computer picks a secret word. Guess it one letter at a time. Every wrong
guess adds a piece to the drawing, and after MAX_WRONG wrong guesses you lose.

    Word:   _ a n _ _ a n
    Wrong:  e s t            (3 of 6)
    Guess a letter:

Play:       .venv/bin/python games/hangman/hangman.py
Run tests:  .venv/bin/pytest games/hangman
"""
import random
from pathlib import Path

WORDS_FILE = Path(__file__).parent / "words.txt"
MAX_WRONG = 6

# STAGES[n] is the drawing after n wrong guesses.
STAGES = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]


def load_words(path: Path) -> list[str]:
    """
    Read one word per line. Strip the spaces around each word, make it lower
    case, and skip blank lines.
    """
    words = []
    with path.open(encoding='utf-8') as file:
        for line in file:
            word = line.strip().lower()
            if word:
                words.append(word)
    return words



def masked(word: str, guessed: set[str]) -> str:
    """
    Show the letters guessed so far and "_" for the rest, separated by spaces:
        masked("hangman", {"a", "n"})  ->  "_ a n _ _ a n"
    """
    return " ".join(c if c in guessed else "_" for c in word)


def wrong_guesses(word: str, guessed: set[str]) -> set[str]:
    """Return the guessed letters that aren't in the word."""
    return guessed - set(word)


def is_solved(word: str, guessed: set[str]) -> bool:
    """True once every letter in the word has been guessed."""
    return set(word) <= guessed


def parse_guess(text: str, guessed: set[str]) -> str | None:
    """
    Turn what the player typed into a lower-case letter: " E " -> "e".
    If it isn't exactly one letter, or that letter was already guessed,
    print why and return None.
    """
    cleaned = text.strip().lower()
    if not cleaned.isalpha():
        print(f"'{text}' is not a letter. Try again.")
        return None
    if len(cleaned) > 1:
        print(f"'{cleaned}' is more than one letter. Pick only one.")
        return None
    if cleaned in guessed:
        print(f"'{cleaned}' was already guessed. Pick a different letter.")
        return None
    return cleaned


def main() -> None:
    """
    Pick a random word from WORDS_FILE and play until it's solved or the
    player reaches MAX_WRONG wrong guesses. Each turn, show the drawing, the
    masked word and the wrong letters, then ask for a guess. At the end, show
    the word and ask whether to play again.
    """
    while True:
        words = load_words(WORDS_FILE)
        random.shuffle(words)
        for word in words:
            guessed = set()
            wrong_guess_count = 0
            while True:
                print(STAGES[wrong_guess_count])
                if wrong_guess_count >= MAX_WRONG:
                    print("GAMEOVER")
                    print(f"The word was '{word}'")
                    break
                print(f"Word:  {masked(word, guessed)}")
                print(f"Wrong: {",".join(sorted(wrong_guesses(word, guessed)))} ({wrong_guess_count} of {MAX_WRONG})")
                while (guess := parse_guess(input("Guess a letter: "), guessed)) is None:
                    continue
                guessed.add(guess)
                if is_solved(word, guessed):
                    print(f"You guessed right! The word was: '{word}'")
                    break
                if guess not in word:
                    wrong_guess_count += 1
            play_again = input("Would you like to play again (y/n): ")
            if "n" in play_again.strip().lower():
                return
            




if __name__ == "__main__":
    main()
