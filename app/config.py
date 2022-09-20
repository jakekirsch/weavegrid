from pydantic import BaseSettings


class Settings(BaseSettings):
    target_dir: str
