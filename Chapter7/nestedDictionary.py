#testing a nested dictionary programm, to work as a user registration

userDataBase = {"NxYt" : {"Name" : "Nicolas", "Age" : "27", "Email" : "nicolas@domain.com"},
                "Fgairy" : {"Name" : "Garry", "Age" : "32", "Email" : "garry@domain.com"},
                "CamTx" : {"Name" : "Carl", "Age" : "19", "Email" : "CarlTheEmployee@domain.com"}}

def AddNewUser(dataBase : dict, userName: str, userData : dict):
    if userData == {}:
        return None
    else:
        if userName in dataBase.keys():
            print("This username already exists")
        else:
            userDataBase[userName] = userData

print(userDataBase.keys())
userName = "NyXs"
userData = {"Name" : "Nash", "Age" : 30, "Email" : "nashWorksHere@domain.com"}
AddNewUser(userDataBase, userName, userData)
print(userDataBase.keys())
print(userDataBase[userName])
