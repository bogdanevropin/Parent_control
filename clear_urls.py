from pathlib import Path
import os 

current_directory = os.getcwd()

source_dir = Path(current_directory)
mask = '_dns'

for file in source_dir.glob(mask):
    os.remove()