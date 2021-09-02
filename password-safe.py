# ---------------------------------
# Main code of password safe

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
master_password = "abcd"
input_password = ""
while(input_password != master_password):
    try:
        input_password = input("\nWhat is your master password?: ")
    
    except ValueError:
                continue

# ---------------------------------------------------------------------
# Greetings and options to user
print("\n---------- Access granted! ----------")

user_option = 0
while(user_option != 1 and user_option != 2 and user_option != 3 and user_option != 4):
    try:
        user_option = int(input("\nWhat would you like to do?\n1 -> Create new password\n2 -> Show specific password\n3 -> Show all passwords\n4 -> Delete password\nYour choice: "))
    
    except ValueError:
                continue

# ---------------------------------------------------------------------
# Next interation with user, based on the previous choice 
u_service, u_login, u_simple_password = "", "", ""

if user_option == 1: #if a new password will be created
    u_service = input("\nWhat is the service? Example: Facebook, Instagram, etc. ")
    u_login = input("What is your login (or email)? ")
    u_simple_password = input("Create a simple password for this service: ")
    new_password = Password(u_service, u_login, u_simple_password)
    #implementar código para criptografar a senha
    #implementar código para salvar a senha na tabela
    #implementar código de copiar a senha para o clipboard
elif user_option == 2: #if a password is being consulted
    u_service = input("\nWhat is the service? Example: Facebook, Instagram, etc. ")
    #implementar código para exibir a senha
    #implementar código de copiar a senha para o clipboard
elif user_option == 3: #if all passwords will be shown
    x = 1 #implementar código para exibir toda a base
else:
    u_service = input("\nWhat is the service? Example: Facebook, Instagram, etc. ")
    #implementar código para deletar a senha da tabela