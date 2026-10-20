"""Print useful parts of a file or directory path."""

from pathlib import Path

user_path = input("Enter a file or directory path: ").strip()
path = Path(user_path).expanduser()

print(f"Absolute path: {path.resolve()}")
print(f"Parent: {path.parent}")
print(f"Name: {path.name}")
print(f"Stem: {path.stem}")
print(f"Suffix: {path.suffix}")
