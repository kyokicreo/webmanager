import os
from pathlib import Path

ROOT_DIR = Path("./storage").resolve()
ROOT_DIR.mkdir(exist_ok=True)


def resolve_path(relative_path: str) -> Path:
    target = (ROOT_DIR / relative_path).resolve()

    if not str(target).startswith(str(ROOT_DIR)):
        raise ValueError("Path is outside of the allowed root directory")

    return target


def list_directory(relative_path: str = "") -> list[str]:
    target = resolve_path(relative_path)

    if not target.exists():
        raise FileNotFoundError("Path does not exist")
    if not target.is_dir():
        raise NotADirectoryError("Path is not a directory")

    result = []
    for entry in target.iterdir():
        name = entry.name
        if entry.is_dir():
            name += "/"
        result.append(name)

    return result


def create_directory(relative_path: str) -> None:
    target = resolve_path(relative_path)

    if target.exists():
        raise FileExistsError("Path already exists")

    target.mkdir(parents=False)


def delete_path(relative_path: str) -> None:
    target = resolve_path(relative_path)

    if not target.exists():
        raise FileNotFoundError("Path does not exist")

    if target.is_dir():
        if any(target.iterdir()):
            raise OSError("Directory is not empty")
        target.rmdir()
    else:
        target.unlink()