from pathlib import Path

current_folder = Path.cwd()  / "Chapter10"
file_name = current_folder / "Poems2.txt"

with open(file_name, "w", encoding="UTF-8") as file_obj:
    file_obj.write("Roses are red\nViolets are blue\n")
    
with open(file_name, "a", encoding="UTF-8") as file_obj:
    file_obj.write("I'm writting notes\nAbout a person called you\n")
    
with open(file_name, "r", encoding="UTF-8") as file_obj:
    content = file_obj.read()

print(content)
