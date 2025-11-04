#this program will add a bullet point to the items added in the clipboard
import pyperclip

clip_board_text = pyperclip.paste()


#add new lines if the file only have a single one
if "\n" not in clip_board_text:
    spaced_clip = clip_board_text.split()
    clip_board_text = "\n".join(spaced_clip)
    
splited_text = clip_board_text.splitlines()

formated_string = ""

##Add bullet points for each line
for line in splited_text:
    formated_string += f"* {line}\n"

pyperclip.copy(formated_string)

