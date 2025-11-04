from pathlib import Path

msg = "Hello, I'm writing into a text file, look how we go"

current_dir = Path.cwd() / "Chapter10"
current_file = current_dir / "fileToRead.txt"
if(current_file.is_file()):
    current_file.write_text("Hello I'm writing into a text file\nIt's a pleasure to finally write somewhere else\nI mean outside the IDE")
else:
    print(f"The file {current_file} doesn't exist in the current directory")

print(current_file.read_text())
