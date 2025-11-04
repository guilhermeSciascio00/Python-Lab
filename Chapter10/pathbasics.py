from pathlib import Path

desktop_path = Path.home() / Path("Desktop/")
new_path = Path(desktop_path) / Path("Spam")
new_path.mkdir()
