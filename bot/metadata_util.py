import subprocess
from pathlib import Path

def set_metadata(input_file: Path, output_file: Path, metadata: dict):
    """
    Use FFmpeg to set metadata on a media file.
    
    Parameters:
    - input_file (Path): Path to the original file.
    - output_file (Path): Path to save the file with metadata.
    - metadata (dict): Dictionary containing metadata fields (title, artist, comment, etc.)
    """

    if not input_file.exists():
        raise FileNotFoundError(f"Input file {input_file} does not exist.")

    ffmpeg_cmd = ["ffmpeg", "-y", "-i", str(input_file)]

    # Add metadata key-value pairs
    for key, value in metadata.items():
        ffmpeg_cmd.extend(["-metadata", f"{key}={value}"])

    # Copy streams (don't re-encode)
    ffmpeg_cmd.extend(["-c", "copy", str(output_file)])

    try:
        subprocess.run(ffmpeg_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] FFmpeg failed: {e}")
        raise
