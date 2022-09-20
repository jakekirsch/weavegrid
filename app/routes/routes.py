from functools import lru_cache
from typing import List, Union
from pathlib import Path
from fastapi import APIRouter, Depends, HTTPException

from app.models.models import DirectoryEntry
from app.controller.controller import list_contents_of_dir, get_contents_of_file
from app.config import Settings


router = APIRouter()


@lru_cache()
def get_settings():
    return Settings()

@router.get(
    "/",
    summary=f"List contents of root directory",
    description="Returns a list of items in the root directory",
    response_model=List[DirectoryEntry]
)
def list_root_contents(settings: Settings = Depends(get_settings)):
    filepath = Path(settings.target_dir)
    try:
        return list_contents_of_dir(settings.target_dir)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail="Item not found")

@router.get(
    "/{path:path}",
    summary="List contents of path",
    description="""If path is a directory, list contents of directory. Otherwise list
    contents of the file""",
    response_model=Union[List[DirectoryEntry], str]
)
def list_path_contents(path: str, settings: Settings = Depends(get_settings)) -> Union[List[DirectoryEntry], str]:
    filepath = Path(settings.target_dir, path)
    try:
        if filepath.is_dir():
            return list_contents_of_dir(filepath)
        else:
            return get_contents_of_file(filepath)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail="Item not found")
