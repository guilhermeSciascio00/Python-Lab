from pathlib import Path

current_path = Path.cwd() / "Chapter10"
current_file = current_path / "fileToRead.txt"

current_file_poem = current_path / "poem.txt"

# if(current_file.is_file()):
#     open_file_to_read = open(current_file, encoding="UTF-8")
    

if(current_file_poem.is_file()):
    open_file_to_read = open(current_file_poem, encoding="UTF-8")
    print(open_file_to_read.readlines())
else:
    print(f"Could't find the file {current_file_poem.name}")
