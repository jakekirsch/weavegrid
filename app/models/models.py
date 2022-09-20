from pydantic import BaseModel

class DirectoryEntry(BaseModel):
    """
    metadata for a file in the directory
    """
    name: str
    owner: str
    size: int
    permissions: int
