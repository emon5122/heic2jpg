# HEIC to JPG Converter

A simple command-line tool to convert HEIC images to JPG format. The tool processes all HEIC files in a specified directory (including subdirectories), converts them to JPG in the same location, and deletes the original HEIC files after successful conversion.

## Features

- 🔄 Batch conversion of HEIC images to JPG
- 📁 Recursive directory scanning (processes subdirectories)
- 🗑️ Automatic deletion of original HEIC files after conversion
- ✅ Progress feedback with conversion status
- 🛡️ Error handling for individual files (continues on errors)
- 📊 Conversion summary report

## Requirements

- Python 3.13+
- pillow
- pillow-heif
- click

## Installation

1. Clone or download this repository

2. Install dependencies using uv (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install pillow pillow-heif click
```

## Usage

Activate the virtual environment (if using uv):
```bash
source .venv/bin/activate
```

Run the converter with a directory path:
```bash
python main.py "/path/to/your/photos"
```

### Example

```bash
python main.py "/home/user/Downloads/Adventure Tour, 2025"
```

Output:
```
Found 12 HEIC file(s) to convert...
✓ Converted 'IMG_0001.HEIC' to 'IMG_0001.jpg'
✓ Deleted original file 'IMG_0001.HEIC'
✓ Converted 'IMG_0002.HEIC' to 'IMG_0002.jpg'
✓ Deleted original file 'IMG_0002.HEIC'
...
Completed: 12/12 files successfully converted and deleted.
```

## Important Notes

⚠️ **Warning**: This tool permanently deletes the original HEIC files after conversion. Make sure you have backups if needed before running the conversion.

## How It Works

1. Scans the specified directory and all subdirectories for HEIC files
2. Opens each HEIC file and converts it to RGB format
3. Saves the converted image as a JPG file in the same directory
4. Deletes the original HEIC file upon successful conversion
5. Reports any errors encountered during the process

## License

This project is open source and available for personal and commercial use.
