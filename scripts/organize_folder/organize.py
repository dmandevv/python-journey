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
from collections import Counter
import itertools

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
    """
    Return the category folder name for a file, based on its extension.
    Upper or lower case doesn't matter. Unknown or missing extensions -> OTHER.
    """
    for name, extensions in CATEGORIES.items():
        if path.suffix.lower() in extensions:
            return name
    return OTHER


def unique_destination(destination: Path, planned_destinations=()) -> Path:
    """
    Return `destination` if nothing exists there yet. Otherwise return the
    first free name of the form "name (1).ext", "name (2).ext", ...
    """
    if not destination.exists() and destination not in planned_destinations:
        return destination
    counter = 0
    while True:      
        counter += 1
        file_name = f"{destination.stem} ({counter}){destination.suffix}"
        file_path = destination.parent / file_name
        if not file_path.exists() and file_path not in planned_destinations:
            return file_path


def plan_moves(folder: Path) -> list[tuple[Path, Path]]:
    """
    Return (source, destination) pairs for every file that should move,
    sorted by source name so the output is predictable.
    Moves nothing: this only works out the plan.
    """
    pairs = []
    planned_destinations = set()
    all_files = [f for f in folder.iterdir() if f.is_file() and not f.name.startswith('.')]
    all_files.sort()
    for file in all_files:
        file_category = category_for(file)
        new_path = folder / file_category / file.name
        dest = unique_destination(new_path, planned_destinations)
        pairs.append((file, dest))
        planned_destinations.add(dest)
    return pairs



def apply_moves(moves: list[tuple[Path, Path]], dry_run: bool) -> None:
    """
    Print each move. Unless `dry_run` is set, also create the category folder
    if needed and move the file.
    """
    if not moves:
        print("No files to move")
        return
    print("Moving files...")
    max_src_len = max((len(src.as_posix()) for src, _ in moves))
    for src, dst in moves:
        print(f"{src.as_posix().ljust(max_src_len)} -> {dst.as_posix()}")
    if dry_run:
        print("Dry run complete, no files moved.")
        return
    for src, dst in moves:
        dst.parent.mkdir(parents=True, exist_ok=True)
        src.rename(dst)


def main(argv: list[str] | None = None) -> None:
    """
    Read the command-line arguments (a folder, and an optional --dry-run flag),
    then plan and apply the moves. `argv` lets tests pass arguments directly;
    None means "use the real command line".
    """
    parser = argparse.ArgumentParser(description="Sort the files in a folder into subfolders by type.")
    parser.add_argument("folder", type=Path, help="Folder to look in")
    parser.add_argument("--dry-run", action="store_true", help="Only prints proposed moves (use this to double check first!)")

    args = parser.parse_args(argv)
    if not args.folder.is_dir():
        parser.error("Folder doesn't exist or is a file.")
    planned_moves = plan_moves(args.folder)
    apply_moves(planned_moves, args.dry_run)


if __name__ == "__main__":
    main()
