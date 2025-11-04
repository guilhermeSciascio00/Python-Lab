from pathlib import Path

current_path = Path.cwd() / "Chapter10"
current_file_path = current_path / "Greetings.txt"

introduction_file = open(current_file_path, "w", encoding="UTF-8")
introduction_file.write("Hello, How are you over there? I'm writing from an IDE \n")
introduction_file.close()

introduction_file = open(current_file_path, "a", encoding="UTF-8")
introduction_file.write("However, I still feeling I'm inside an text editor, hmm\n")
introduction_file.close()
