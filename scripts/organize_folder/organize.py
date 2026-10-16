"""
Sort the files in a folder into subfolders by type.

    photo.JPG    ->  Images/photo.JPG
    report.pdf   ->  Documents/report.pdf
    setup.exe    ->  Other/setup.exe

Only files directly inside the folder are moved. Subfolders and hidden files
(names starting with ".") are left alone. A file is never overwritten: if
the destination name is taken, the new file becomes "name (1).ext".

Usage:
    .venv/bin/python scripts/organize_folder/organize.py ~/Downloads --dry-run
    .venv/bin/python scripts/organize_folder/organize.py ~/Downloads

Run tests:  .venv/bin/pytest scripts/organize_folder
"""
import argparse
from pathlib import Path

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".md", ".odt"},
    "Spreadsheets": {".xls", ".xlsx", ".csv", ".ods"},
    "Archives": {".zip", ".tar", ".gz", ".7z", ".rar"},
    "Audio": {".mp3", ".wav", ".flac", ".ogg"},
    "Video": {".mp4", ".mkv", ".mov", ".avi"},
    "Code": {".py", ".js", ".html", ".css", ".json", ".sh"},
}
OTHER = "Other"


def category_for(path: Path) -> str:
    for cat in CATEGORIES.items():
        if (path.suffix.lower() in cat[1]):
            return cat[0]
    return OTHER


def unique_destination(destination: Path) -> Path:
    if destination.exists() == False:
        return destination
    counter = 0
    while(True):
        counter += 1
        file_name = f"{destination.stem} ({counter}){destination.suffix}"
        file_path = destination.parent / file_name
        if file_path.exists() == False:
            return file_path


def plan_moves(folder: Path) -> list[tuple[Path, Path]]:
    """
    Return (source, destination) pairs for every file that should move,
    sorted by source name so the output is predictable.
    Moves nothing: this only works out the plan.
    """
    pass


def apply_moves(moves: list[tuple[Path, Path]], dry_run: bool) -> None:
    """
    Print each move. Unless `dry_run` is set, also create the category folder
    if needed and move the file.
    """
    pass


def main(argv: list[str] | None = None) -> None:
    """
    Read the command-line arguments (a folder, and an optional --dry-run flag),
    then plan and apply the moves. `argv` lets tests pass arguments directly;
    None means "use the real command line".
    """
    pass


if __name__ == "__main__":
    main()
