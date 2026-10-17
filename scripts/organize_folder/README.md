# Organize Folder

Sorts the files in a folder into subfolders by type.

## Example

Stuff/photo.JPG    ->  Stuff/Images/photo.JPG  
Stuff/report.pdf   ->  Stuff/Documents/report.pdf  
Stuff/setup.exe    ->  Stuff/Other/setup.exe  

## How to run

```
python organize.py "FOLDER_PATH" --dry-run
```

Once files are confirmed, run again without ```--dry-run```

```
python organize.py "FOLDER_PATH"
```

## Tests

```
pytest test_organize.py
```