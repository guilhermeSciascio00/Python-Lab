import shelve
from pathlib import Path

current_folder = Path.cwd() / "Chapter10"

shelf_file = shelve.open(current_folder / "MyData")

shelf_file["Fruits"] = ["Orange", "Banana", "Apple"]
shelf_file.close()
