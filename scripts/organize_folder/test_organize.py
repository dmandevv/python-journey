"""
Every test gets its own empty temporary folder from pytest (`tmp_path`),
so nothing here ever touches real files.
"""
from pathlib import Path

import pytest

from organize import OTHER, apply_moves, category_for, main, plan_moves, unique_destination


def make_files(folder: Path, *names: str) -> None:
    for name in names:
        (folder / name).write_text(name)


# --- category_for -----------------------------------------------------------

@pytest.mark.parametrize(
    "name, expected",
    [
        ("photo.jpg", "Images"),
        ("PHOTO.JPG", "Images"),        # case doesn't matter
        ("report.pdf", "Documents"),
        ("data.csv", "Spreadsheets"),
        ("backup.tar.gz", "Archives"),  # the last extension decides
        ("setup.exe", OTHER),           # unknown extension
        ("README", OTHER),              # no extension at all
    ],
)
def test_category_for(name, expected):
    assert category_for(Path(name)) == expected


# --- unique_destination -----------------------------------------------------

def test_unique_destination_when_free(tmp_path):
    assert unique_destination(tmp_path / "a.txt") == tmp_path / "a.txt"


def test_unique_destination_adds_a_number(tmp_path):
    make_files(tmp_path, "a.txt")
    assert unique_destination(tmp_path / "a.txt") == tmp_path / "a (1).txt"


def test_unique_destination_finds_the_next_free_number(tmp_path):
    make_files(tmp_path, "a.txt", "a (1).txt", "a (2).txt")
    assert unique_destination(tmp_path / "a.txt") == tmp_path / "a (3).txt"


# --- plan_moves --------------------------------------------------------------

def test_plan_moves(tmp_path):
    make_files(tmp_path, "b.pdf", "a.png", "c.unknown")
    assert plan_moves(tmp_path) == [
        (tmp_path / "a.png", tmp_path / "Images" / "a.png"),
        (tmp_path / "b.pdf", tmp_path / "Documents" / "b.pdf"),
        (tmp_path / "c.unknown", tmp_path / OTHER / "c.unknown"),
    ]


def test_plan_moves_leaves_folders_and_hidden_files_alone(tmp_path):
    (tmp_path / "Projects").mkdir()
    make_files(tmp_path, ".bashrc", "Projects/inside.png")
    assert plan_moves(tmp_path) == []


def test_plan_moves_never_overwrites(tmp_path):
    (tmp_path / "Images").mkdir()
    make_files(tmp_path, "a.png", "Images/a.png")
    assert plan_moves(tmp_path) == [
        (tmp_path / "a.png", tmp_path / "Images" / "a (1).png"),
    ]


def test_plan_moves_on_an_empty_folder(tmp_path):
    assert plan_moves(tmp_path) == []


# --- apply_moves -------------------------------------------------------------

def test_dry_run_moves_nothing(tmp_path, capsys):
    make_files(tmp_path, "a.png")
    apply_moves(plan_moves(tmp_path), dry_run=True)
    assert (tmp_path / "a.png").exists()
    assert not (tmp_path / "Images").exists()
    assert "a.png" in capsys.readouterr().out      # but it says what it would do


def test_apply_moves_moves_files_and_keeps_content(tmp_path):
    make_files(tmp_path, "a.png", "b.pdf")
    apply_moves(plan_moves(tmp_path), dry_run=False)
    assert not (tmp_path / "a.png").exists()
    assert (tmp_path / "Images" / "a.png").read_text() == "a.png"
    assert (tmp_path / "Documents" / "b.pdf").read_text() == "b.pdf"


# --- main --------------------------------------------------------------------

def test_main_end_to_end(tmp_path):
    make_files(tmp_path, "a.png", "notes.txt")
    main([str(tmp_path)])
    assert (tmp_path / "Images" / "a.png").exists()
    assert (tmp_path / "Documents" / "notes.txt").exists()


def test_main_dry_run_flag(tmp_path):
    make_files(tmp_path, "a.png")
    main([str(tmp_path), "--dry-run"])
    assert (tmp_path / "a.png").exists()
