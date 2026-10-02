# Progress

**Where the Python Journey stands.** This is block 2 of the daily routine. Claude reads this file to resume the block and updates it as work gets done.

---

## Position

**Set up 2026-10-02.** **Python 3.14.5**, with a virtual environment in `.venv/` (rebuilt from 3.12 the same day. 3.12 is Ubuntu's system Python and stays installed, because removing it would break the OS) and `pytest` installed (listed in `requirements.txt`). Git repo started on `main`; it will be a **public repo for employers to see**. `pygame` gets installed when Pong starts.

**Level check so far:** Two Sum was solved quickly by brute force, with clean code and correct edge cases. The single-pass version using a dictionary was new and was shown with an explanation. **Next challenges should mix in common patterns** (hash map, two pointers, sliding window), explained when they first come up.

**⏭️ Next session:** warm-up challenge 002, then start tic-tac-toe in the terminal (`games/tic_tac_toe/`). Still to decide: two players or against the computer, and whether you plan the structure or Claude outlines the functions. First commit made 2026-10-02.

## Track status

| Track | Done | Current |
|---|---|---|
| Challenges | 1 | 001 Two Sum ✅ |
| Games | 0 | **tic-tac-toe** in progress (two players, keypad 1–9), then Pong |
| Scripts | 0 | none yet |

## Ideas backlog

- **Games:** tic-tac-toe, Pong, Snake, Hangman, Blackjack, Minesweeper
- **Scripts:** sort Downloads into folders by file type, bulk-rename files, find duplicate files, back up a folder with a timestamp, a CSV expense summary, a disk usage report

---

## Daily log

### 2026-10-02
- Created the directory: `README.md`, this file, `challenges/`, `games/`, `scripts/`
- Environment: `.venv/` with `pytest`, plus `.gitignore` and `requirements.txt`. `git init` on `main`
- `.venv/` rebuilt on Python 3.14.5. VS Code needs the interpreter path set by hand when the window is open on the parent folder
- **Challenge 001 Two Sum ✅**: brute force O(n²) first, then a single pass with a dictionary, O(n). Both kept in the file
  - Tests parametrized with `pytest.mark.parametrize`, so both functions run against every case (8 tests)
  - Main work skipped today; moved on to the homelab
  - Learned: `enumerate()` instead of `range(len(...))` when you need the index and the value; a dictionary of values already seen turns "search for a partner" into a single lookup; check before storing so an element can't pair with itself
