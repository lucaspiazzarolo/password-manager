# ---------------------------------
# Main code of password safe
import hashlib #library that will be used for the hashed password
import functions as f

# ---------------------------------------------------------------------
# Create class "Password"
class Password:
    def __init__(self, u_service, u_login, u_simple_password):
        self.u_service = u_service
        self.u_login = u_login
        self.u_simple_password = u_simple_password

# ---------------------------------------------------------------------
# Require master password
print("\n---------- Welcome to your password safe! ----------")
master_password = "b2e618d56fe1074893f768d24de12017fb28df02" #You should run the 'hash-engine.py' script and replace this with your hashed password
salt = "x\¨Ngy7" #salt used both in 'hash-engine.py' and here

hashed_password = ""
while(hashed_password != master_password):
    try:
        input_password = input("\nWhat is your master password?: ") #checks for input password
        hashed_password = hashlib.sha1((input_password + salt).encode('utf-8')).hexdigest() #hashes input password
    
    except ValueError:
        continue

# ---------------------------------------------------------------------
# Greetings and options to user
print("\n---------- Access granted! ----------")

user_option = 0
while(user_option != 1 and user_option != 2 and user_option != 3 and user_option != 4):
    try:
        user_option = int(input("\nWhat would you like to do?\n1 -> Generate secure password\n2 -> Store existing password \n3 -> Show all stored logins\n4 -> Show specific password\n5 -> Delete password\n6 -> Exit\nYour choice: "))
    
    except ValueError:
                continue

# ---------------------------------------------------------------------
# Next interation with user, based on the previous choice 
u_service, u_login, u_simple_password = "", "", ""

if user_option == 1: #if a new password will be created
    print("\n---------- Let's create a new password! ----------")
    u_service = input("\nWhat is the service? Example: Facebook, Instagram, etc. ") #service that will store the new password
    u_login = input("What is your login (or email)? ") #login info
    str_password = f.generate_password() #calls function to generate the password
    new_password = Password(u_service, u_login, str_password) #create new password object
    #implementar código para criptografar a senha
    #implementar código para salvar a senha na tabela
    #implementar código de copiar a senha para o clipboard

elif user_option == 2: #if an existing password will be stored
    print("\n---------- Let's store your existing password! ----------")
    u_service = input("\nWhat is the service? Example: Facebook, Instagram, etc. ") #service that will store the new password
    u_login = input("What is your login (or email)? ") #login info
    str_password = input("What is your password? ") #existing password info
    new_password = Password(u_service, u_login, str_password) #create new password object
    #implementar código para criptografar a senha
    #implementar código para salvar a senha na tabela

elif user_option == 3: #if all stored logins will be shown
    x = 1 #implementar código para exibir toda a base

elif user_option == 4: #if a specific password needs to be shown
    u_service = input("\nWhat is the service? Example: Facebook, Instagram, etc. ")
    #implementar código para descriptografar a senha da tabela
    #trazer a senha
    #copiar para clipboard

elif user_option == 5: #if a specific password needs to be deleted from the database
    u_service = input("\nWhat is the service? Example: Facebook, Instagram, etc. ")
    #implementar código para deletar a linha na tabela