import os
from typing import List
from pathlib import Path

from decouple import config
from fastapi import APIRouter

from app.models.models import DirectoryEntry
from app.controller.controller import list_contents_of_dir, get_contents_of_file

# settings/config
root_dir = Path(config('TARGET_DIR'))

router = APIRouter()

@router.get(
    "/",
    summary="List contents of root directory",
    description="this is a description"
)
def list_root_contents() -> List[DirectoryEntry]:
    # TODO: check to make sure root directory is valid
    return list_contents_of_dir(root_dir)

@router.get(
    "/{path:path}",
    summary="List contents of path",
    description="""If path is a directory, list contents of directory. Otherwise list
    contents of the file"""
)
def list_path_contents(path: str) -> List[DirectoryEntry]:
    print(path)
    # TODO: check to make sure path is valid
    filepath = Path(root_dir, path)
    if os.path.isdir(filepath):
        return list_contents_of_dir(filepath)
    else:
        return get_contents_of_file(filepath)
