
def is_phone_number(text : str):
    #Checking if the phone number has 12 digits
    if len(text) != 12:
        return False
    
    #Checking the first three digits
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    
    #The forth character mush be a dash
    if text[3] != "-":
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    
    if text[7] != "-":
        return False
    
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    return True


phone_number = "415-555-2222"
print(f"Is {phone_number} valid? {is_phone_number(phone_number)}")

phone_number2 = "333-aa4-47as"
print(f"Is {phone_number2} valid? {is_phone_number(phone_number2)}")
