#the program will ask the user to createa a user(email and password)
#But the program will also check if the passowrd is alphanum only

registred_users = {"Admin@gmail.com" : {"Username" : "Admin000", "Password" : "x7A543Bcfas"}}
first_time_user = True

def registrer_user(email, username, password):
    registred_users[email] = {"Username" : username, "Password" : password}
    
    
print("Welcome to the XO System")
while True:
    if first_time_user:
        print("I see that it's your first time using the system")
        print("Let's create an account")
        first_time_user = False
        print("What's your email?")
        while True:
            email = input(">").lower()
            if " " not in email:
                break
            print("No spaces in the email")
        print("What's your user name?(No spaces allowed)")
        while True:
            user_name = input(">")
            if user_name.isalnum():
                break
            print("The name must not have spaces")
        print(f"{user_name} what's your password?(No spaces allowed)")
        while True:
            pass_word = input(">")
            if " " not in pass_word:
                break
            print("The password must not have spaces!!")
        if email and user_name and pass_word:
            registrer_user(email, user_name, pass_word)
            print("User was suceffuly created")
            print("Time to Log in")
    
    print("Email: ")
    check_email = input(">").lower()
    while True:
        if check_email in registred_users.keys():
            print("Password: ")
            check_password = input(">")
            if check_password == registred_users[check_email]["Password"]:
                print(f"Welcome {registred_users[check_email]["Username"]} to the XO System ")
                print("Have a good time !")
                break
            else:
                print("Invalid password, try again")
        else:
            print("Wrong email, please try again")       
    break
