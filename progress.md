# Progress

**Where the Python Journey stands.** This is block 2 of the daily routine. Claude reads this file to resume the block and updates it as work gets done.

---

## Position

**Set up 2026-10-02.** **Python 3.14.5**, with a virtual environment in `.venv/` (rebuilt from 3.12 the same day. 3.12 is Ubuntu's system Python and stays installed, because removing it would break the OS) and `pytest` installed (listed in `requirements.txt`). Git repo started on `main`; it will be a **public repo for employers to see**. `pygame` gets installed when Pong starts.

**Level check so far:** Two Sum was solved quickly by brute force, with clean code and correct edge cases. The single-pass version using a dictionary was new and was shown with an explanation. **Next challenges should mix in common patterns** (hash map, two pointers, sliding window), explained when they first come up.

**⏭️ Next session:** warm-up challenge 007, then carry on with the **organiser script** (`scripts/organize_folder/`): all 5 functions are still stubs, 1 of 18 tests passes. Suggested order: `category_for` → `unique_destination` → `plan_moves` → `apply_moves` → `main` (`argparse` is new). Try it on a throwaway folder with `--dry-run` before any real one.

**Optional polish on Pong** (it works, so none of this blocks anything):
- The wall check for the paddles is copied once per paddle in `main`; `clamp_ip(bounds)` in `Paddle.update` replaces both copies
- `Paddle.get_direction()` is missing `self` (it only matters if the base version is ever called)
- `ComputerPaddle` compares top edges with no dead zone, so it shakes and can't be beaten. Compare centres, add a dead zone, or give it a slower speed
- Unused `import sys` and `in_bounds`; paddles are placed by their top-left corner (use `get_frect(center=(x, y))`)

**Optional polish on tic-tac-toe** (it works, so none of this blocks anything): `again.isalpha` is missing `()`, so it's always true; `"y" in again` also matches "no way"; use `return` instead of `exit(0)` in `main`; the docstring at the top still describes the old keypad and list design.

**Tools found today:** the REPL (`.venv/bin/python`), `python -c`, `importlib.reload`, `input()`. Not done yet: installing IPython for autoreload.

## Track status

| Track | Done | Current |
|---|---|---|
| Challenges | 7 | 001 Two Sum ✅ · 002 Valid Palindrome ✅ (two-pointer version fixed by Claude) · 003 Reverse In Place ✅ · 004 Max Sum Window ✅ · 005 Valid Parentheses ✅ · 006 Binary Search ✅ · 007 Valid Anagram ✅ |
| Games | 2 | tic-tac-toe ✅ · Pong ✅ |
| Scripts | 0 | **organize_folder** in progress (sort a folder into subfolders by type) |

## Ideas backlog

- **Games:** tic-tac-toe, Pong, Snake, Hangman, Blackjack, Minesweeper
- **Scripts:** sort Downloads into folders by file type, bulk-rename files, find duplicate files, back up a folder with a timestamp, a CSV expense summary, a disk usage report

---

## Daily log

### 2026-10-15
- **Challenge 007 Valid Anagram ✅**: three versions, all yours (`sorted`, a hand-built count dictionary, `Counter`), each run against 10 cases (30 tests)
  - Learned: counting with `d.get(k, 0) + 1`; `collections.Counter`; **`a = b = {}` makes one dictionary with two names**, not two (it made every pair count as an anagram until it was split)
  - VS Code: IntelliSense stopped because the Python extensions weren't running in the window (no Pylance activity in the logs). Fix: enable them for WSL, re-select `.venv`, reload the window. Also remove the stale `python.pythonPath: /usr/bin/python` user setting, which points at a file that doesn't exist

### 2026-10-12
- **Challenge 006 Binary Search ✅**, 11 tests including a million-item list. Written by you and right first time: `low <= high`, and both boundaries move past `mid`, so the two-item case can't loop
- **First script started: `scripts/organize_folder/`.** Claude wrote stubs and 18 tests: `category_for`, `unique_destination`, `plan_moves`, `apply_moves`, and `main` with `argparse` and `--dry-run`. All tests run in pytest's `tmp_path`, so they never touch real files

### 2026-10-10
- **Challenge 005 Valid Parentheses ✅** (stack), 14 tests, rated 8/10: correct and O(n), and it handles both edge cases (closing with nothing open, left unclosed). **Design call (yours): spaces are ignored**, with tests for `"()  []"` and `"  "`. Remaining nit: any other non-bracket character is pushed as if it were an opening bracket
  - Learned: a list as a stack (`append`, `pop`, `[-1]`); `is None` rather than `== None`; `not stack` for "empty"; when a test fails, decide whether the **code or the rule** is wrong before changing either
- **Pong ✅ done**: scoring (left wall → player 2, right wall → player 1), the score drawn with `font.render` and `blit`, a 2-second serve pause, the ball pushed out after every bounce, and the speed reset each point. **Your own addition:** random acceleration (`random.uniform`) so rallies speed up unpredictably
  - Bugs found on the way: `score_pause_timer = …` without `self.` made a local variable, so the pause never started; `rect.center = x` then `= y` crashes with `TypeError` (it takes a pair: `(x, y)`). Verified: `reset()` now runs cleanly and all 89 tests pass
  - Learned: `max(0, t - dt)` to clamp a value; an early `return` instead of nesting in `else`; text in pygame is render-then-blit

### 2026-10-08
- **Pong: the ball and the paddle classes.** `Ball` with a `Vector2` velocity; it bounces off the walls and both paddles. `Paddle` split into `PlayerPaddle` and `ComputerPaddle` (your idea), where only `get_direction()` differs
  - Learned: `or` returns the first **truthy** value, and `-1` is truthy while `0` isn't, so `collidelist(a) or collidelist(b)` skipped the second check and missed the top wall. Use `colliderect` for single objects. Also learned the template-method pattern and `super().__init__()`, and that `keys[down] - keys[up]` gives -1, 0 or 1

### 2026-10-07
- **Challenge 004 Max Sum of k Consecutive ✅**: both versions written by you, 14 tests. The sliding window starts from the first window's sum, then each step adds `nums[i+k-1]` and subtracts `nums[i-1]`
  - Learned: `:=` binds more loosely than `>`, so write `(s := sum(w)) > best`; `a if c else b` always needs an `else`, so use `max(a, b)` instead; starting the sliding window with the first window's sum also handles the all-negative case
- **Pong started**: installed `pygame-ce` 2.5.8 (the actively maintained fork; still `import pygame`) into `.venv` and added it to `requirements.txt`. `games/pong/pong.py` has the bare game loop: events → update → draw at 60 FPS. WSLg provides the display
- **Pong: paddles move and stop at the walls.** You built a `Paddle` sprite class and a sprite group, and use `dt` so speeds are in pixels per second
  - Learned: `Rect` stores whole numbers only, so small `dt` moves round away (up worked, down didn't); `FRect` keeps the fractions. Collision **detection** (`collidelist`) and collision **response** (moving the object back out) are separate steps. pygame's y axis points down

### 2026-10-06
- **Challenge 003 Reverse a List In Place ✅**: two pointers, written from scratch with no help, and correct first time. That's the pattern from 002 learned
- **Tic-tac-toe ✅ done**: final board shown on a win or draw, play again (y/n), the loser of each game starts the next
- Added `pytest.ini`: plain `pytest` was finding only `test_*.py` files and **skipping every challenge**. `.venv/bin/pytest` now runs everything: **61 tests, all passing**
- **Tic-tac-toe playable, 27/27 tests pass.** Fixed: the `parse_move` index (`(row - 1) * size + (column - 1)`) and its off-by-one range; `winner` via slices (`tiles[n::size]` for columns, `[::size+1]` and `[size-1:-1:size-1]` for diagonals) plus a `line_is_winner` helper using `all()`; the last row and column were missed by `range(size - 1)`
  - **Design call (yours):** `is_draw` → **`is_full`**, because the game loop already checks `winner` first. The name now says exactly what it does, and `winner` runs once per turn
  - Learned: conditional expressions (`a if cond else b`), `:=`, step slices, `all()` with a generator expression

### 2026-10-03
- **Challenge 002 Valid Palindrome ✅**: you wrote the clean-and-reverse version. The two-pointer version looped forever; Claude fixed it on request. Both functions are tested (18 tests)
  - Bugs in the two-pointer version: the pointers never moved after a match; `a == b is False` is a chained comparison (`a == b and b is False`), so use `!=`; no `.lower()`; the skip loops ran past the end of the string on `" "` and `""`
  - **Worth revisiting:** write a two-pointer solution from scratch with no help (e.g. reverse a list in place)
- **Tic-tac-toe tests rewritten for your design** (`Board`, `TILE`, row and column input, `winner` returns a `TILE`): 25 tests, 13 passing. `new_board` and `render` pass. The `parse_move` failures are the range and index bugs, and `winner` and `is_draw` aren't written yet

### 2026-10-02
- Created the directory: `README.md`, this file, `challenges/`, `games/`, `scripts/`
- Environment: `.venv/` with `pytest`, plus `.gitignore` and `requirements.txt`. `git init` on `main`
- `.venv/` rebuilt on Python 3.14.5. VS Code needs the interpreter path set by hand when the window is open on the parent folder
- **Challenge 001 Two Sum ✅**: brute force O(n²) first, then a single pass with a dictionary, O(n). Both kept in the file
  - Tests parametrized with `pytest.mark.parametrize`, so both functions run against every case (8 tests)
  - Moved to the homelab, then came back after it
- **Tic-tac-toe started**: Claude wrote the stubs and 21 tests; you rewrote it around a `Board` class and a `TILE` enum. Board, render and move input are written; win and draw checks still to do
  - Learned: `enumerate()` instead of `range(len(...))` when you need the index and the value; a dictionary of values already seen turns "search for a partner" into a single lookup; check before storing so an element can't pair with itself
