import click
from PIL import Image
from pillow_heif import register_heif_opener
from pathlib import Path
import os

# Register the HEIF opener
register_heif_opener()

def convert_heic_directory(input_dir):
    """
    Converts all HEIC images in a directory to JPG in the same location and deletes the original HEIC files.
    
    Args:
        input_dir (str): The path to the directory containing .heic files.
    """
    input_path = Path(input_dir)
    
    if not input_path.exists():
        click.echo(f"Error: Directory '{input_dir}' does not exist.", err=True)
        return
    
    if not input_path.is_dir():
        click.echo(f"Error: '{input_dir}' is not a directory.", err=True)
        return
    
    # Find all HEIC files
    heic_files = list(input_path.rglob("*.[hH][eE][iI][Cc]"))
    
    if not heic_files:
        click.echo(f"No HEIC files found in '{input_dir}'")
        return
    
    click.echo(f"Found {len(heic_files)} HEIC file(s) to convert...")
    
    # Iterate over all files in the input directory
    converted_count = 0
    for heic_path in heic_files:
        try:
            image = Image.open(heic_path)
            image = image.convert('RGB')
            
            # Construct the new file path for the JPG in the same directory
            jpg_path = heic_path.parent / (heic_path.stem + '.jpg')
            
            # Save the new JPG file
            image.save(jpg_path, 'JPEG')
            click.echo(f"✓ Converted '{heic_path.name}' to '{jpg_path.name}'")
            
            # Delete the original HEIC file after successful conversion
            os.remove(heic_path)
            click.echo(f"✓ Deleted original file '{heic_path.name}'")
            converted_count += 1
        except Exception as e:
            click.echo(f"✗ Error converting '{heic_path.name}': {e}", err=True)
    
    click.echo(f"\nCompleted: {converted_count}/{len(heic_files)} files successfully converted and deleted.")


@click.command()
@click.argument('directory', type=click.Path(exists=False))
def main(directory):
    """
    Convert all HEIC images in DIRECTORY to JPG format.
    
    The converted JPG files will be saved in the same directory as the original HEIC files,
    and the original HEIC files will be deleted after successful conversion.
    
    Example: python main.py "/path/to/photos"
    """
    convert_heic_directory(directory)


if __name__ == "__main__":
    main()
