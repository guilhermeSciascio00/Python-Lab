import pyperclip


pyperclip.copy("I Like burgers")
msg = f"Your clip board has the following value: {pyperclip.paste()}"
print(msg)
