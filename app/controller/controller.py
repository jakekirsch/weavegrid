import os
from typing import List
from pathlib import Path

from app.models.models import DirectoryEntry


def list_contents_of_dir(dirpath: Path) -> List[DirectoryEntry]:
    """
    Returns a list
    """
    contents = []
    entries = [Path(x.path) for x in os.scandir(dirpath)]
    for entry_path in entries:
        contents.append(DirectoryEntry(name=entry_path.name,
                                       owner=entry_path.owner(),
                                       size=entry_path.stat().st_size,
                                       permissions=oct(entry_path.stat().st_mode)[-3:]))
    return contents


def get_contents_of_file(filepath: Path) -> str:
    """
    Returns the contents of the filepath into a string
    """
    file_contents = ''
    with open(filepath) as f:
        for line in f:
            file_contents += line
    return file_contents
