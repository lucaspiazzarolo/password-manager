# ---------------------------------
# Main code of password safe
import hashlib #library that will be used for the hashed password
import functions as f
import secrets
import string    

# ---------------------------------------------------------------------
# Require master password
print("\n---------- Welcome to your password safe! ----------")
master_password = "b2e618d56fe1074893f768d24de12017fb28df02" #You should run the 'hash-engine.py' script and replace this with your hashed password
master_password = master_password + ''.join(secrets.choice(string.ascii_letters + string.digits)) #returns password
salt = "x\¨Ngy7" #salt used both in 'hash-engine.py' and here
peppers = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"] #possible peppers ahead of master password

hashed_password = ""
correct_password = False

while correct_password == False: #while user didn't input the correct password
    try:
        input_password = input("\nWhat is your master password?: ") #checks for input password
        hashed_password = hashlib.sha1((input_password + salt).encode('utf-8')).hexdigest() #hashes input password
        
        for pepper in peppers: #loop through all possible peppers
            if (hashed_password + pepper) == master_password:
                correct_password = True

    except ValueError:
        continue

# ---------------------------------------------------------------------
# Greetings and options to user
print("\n---------- Access granted! ----------")

user_option = 0

while(user_option != 7): #loop so the user can perform many actions in one login.
    user_option = 0
    while not(user_option >= 1 and user_option <= 7):
        try:
            user_option = int(input("\nWhat would you like to do?\n1 -> Generate secure password\n2 -> Store existing password \n3 -> Display all stored logins\n4 -> Display specific password\n5 -> Update register\n6 -> Delete register\n7 -> Exit\nYour choice: "))
        
        except ValueError:
                    continue

    # ---------------------------------------------------------------------
    # Next interation with user, based on the previous choice 
    u_service, u_login, u_simple_password = "", "", "" #check if needs to be these variables.

    if user_option == 1: #if a new password will be created
        print("\n---------- Let's create a new password! ----------")
        u_service = input("\nWhat is the service? Example: Facebook, Instagram, etc.: ") #service that will store the new password
        service_registered = f.check_if_registered(u_service) #checks if service is already registered
        
        if service_registered == True: #if it is an already registered service
            print("\n'{}' already has a password stored in the database. \n".format(u_service))
            print("\n---------- Please select a new option below ----------")
        
        if service_registered == False: #if it is a new service
            u_login = input("What is your login (or email)? ") #login info
            str_password = f.generate_password() #calls function to generate the password
            f.copy_to_clipboard(str_password) #copies password to clipboard
            c_password = f.encrypt_string(str_password) #encrypts password        
            f.write_table(u_service, u_login, c_password) #writes the password in the table
            print("\n---------- Password successfully inserted into table and copied to clipboard! ----------")

    elif user_option == 2: #if an existing password will be stored
        print("\n---------- Let's store your existing password! ----------")
        u_service = input("\nWhat is the service? Example: Facebook, Instagram, etc.: ") #service that will store the new password
        service_registered = f.check_if_registered(u_service) #checks if service is already registered

        if service_registered == True: #if it is an already registered service
            print("\n'{}' already has a password stored in the database. \n".format(u_service))
            print("\n---------- Please select a new option below ----------")
        
        if service_registered == False: #if it is a new service
            u_login = input("What is your login (or email)? ") #login info
            str_password = input("What is your password? ") #existing password info
            f.copy_to_clipboard(str_password) #copies password to clipboard
            c_password = f.encrypt_string(str_password) #encrypts password
            f.write_table(u_service, u_login, c_password) #writes the password in the table
            print("\n---------- Password successfully inserted into table and copied to clipboard! ----------")

    elif user_option == 3: #if all stored logins will be shown
        print("\n---------- Retrieving all logins from database! ----------\n")
        f.show_logins() #calls function that shows all logins from database

    elif user_option == 4: #if a specific password needs to be shown
        print("\n\n---------- Let's retrieve your password! ----------\n")
        u_service = input("What is the service? Example: Facebook, Instagram, etc.: ")
        f.show_password(u_service)

    elif user_option == 5: #if a specific register needs to be updated from the database
        print("\n\n---------- Let's update your register! ----------\n")
        u_service = input("\nWhat is the service? Example: Facebook, Instagram, etc.: ")
        f.change_table_row(u_service)
        #implementar código para deletar a linha na tabela
    
    elif user_option == 6: #if a specific register needs to be deleted from the database
        print("\n\n---------- Let's delete your register! ----------\n")
        u_service = input("\nWhat is the service? Example: Facebook, Instagram, etc.: ")
        registered = f.check_if_registered(u_service)
        f.delete_table_row(u_service)
        if  registered:
            print("\n---------- {} register successfully deleted! ----------\n".format(u_service))

    elif user_option == 7: #exit
        print("\n\n---------- See you later! ----------\n")