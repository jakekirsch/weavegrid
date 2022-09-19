from pydantic import BaseModel

class DirectoryEntry(BaseModel):
    name: str
    owner: str
    size: int
    permissions: int
