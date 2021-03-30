# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# https:// web address
# TODO STATUS:    Working 2021 Mar 25...
# TODO SUBMITTED: No
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# This is a simple username/password login code.
# old: https://github.com/PdxCodeGuild/Programming102/blob/master/labs/user_login.md
# new: https://github.com/PdxCodeGuild/Programming102/blob/master/labs/lab5.md
# new early 2021: adding 5.4 and 5.5 , multiple users and user_exists_check()... 
# see bottom
# ##################



# make user_profiles dictionary, base username:password
user_profiles = {
    'username':'john',
    'password':'apples',
}

# make login function (main) function return true if match any keypair, otherwise false and error
def login(input_username,input_password):
    actual_password = user_profiles.get('password')

    if input_password == actual_password:
        return True
    else:
        return False
        
def main():    
    welcome = 'Welcome to Website Login v1.2. Please do not hack.'
    print(welcome)
            
    input_username = input('Please enter your username: ')
    # input_username = 'john' # FOR TESTING

    input_password = input('Please enter your password: ')
    # input_password = 'appleaoeus' # FOR TESTING
    
    attempted_logins_counter = 1
    while attempted_logins_counter < 3:
        if login(input_username,input_password) == True: 
            print(f'Login Successful! Welcome, {input_username}!')
            break

        else:
            attempted_logins_counter += 1
            print('Login Failed! Do not hack!')            

            #retry... do i really need to code this like this exactly?
            input_username = input('Please try your username again: ')
            input_password = input('Please try your password again: ')

            #do I really need to run this again like this?
            if login(input_username,input_password) == True: 
                print(f'Login Successful! Welcome, {input_username}!')
                break

        if attempted_logins_counter == 3:
                print('Too many attempted login attempts. Try again in 24 hours, or contact your system administrator!')

main()

# print('end code #######################') #REMOVE helps me know if the code got to the end or finished elsewhere...

# 5.4
# Add support for multiple users.
# A few things will need to change:

#     Instead of one profile, you will need a list of profiles. Each profile will be a dictionary containing key : value pairs with the keys of username and password.
#     When the user enters their username and password attempts, loop through the list of profiles, pass each profile one at time into the login() function along with the username_attempt and password_attempt.
#     If the username_attempt and password_attempt match the values at the keys of username and password current profile, the login() function will return that True and that user will be logged in. Otherwise, it will return False.

# 5.5 - Extra Challenge
#     Define a function called create_user() which:
#         prompts the user for a username and password.
#         checks to see if the username already exists in the profiles list using the user_exists() function
#         If the username is unique and doesn't appear in the profiles list, .append() it to the profiles list.
#     Define a function called user_exists() which will:
#         loop through each profile in the profiles list
#         check to see if the username the user entered already exists within one of the profile dictionaries.
#     If a user with that username already exists, return True, otherwise return False
#     Integrate the create_user() function into your REPL to allow the user to create a new username.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Profiles list:

# username: gandalfTheGrey
# password: noneShallPass!

# username: bilboBaggins
# password: theShire123

# username: iAmSmeagol
# password: myPrecious!

# Lab 5 - User Login

# Back to Syllabus

# Create a REPL which allows a user to 'log in'.

# Please complete the sections in order. Create a working version of 5.1 before attempting 5.2, etc. This will make your life easier. You may also want to consider creating separate .py files for each version, so you can refer back to previous working versions.
# 5.1

# Create a dictionary called profile

# The profile should contain two key : value pairs with keys of username and password and values of your choosing. They will represent a username and password for a single user.

# username - gandalfTheGrey
# password - noneShallPass!

# Do not create your profile with the user's username as the key and their password as the value as below:

# 'gandalfTheGrey':'noneShallPass'

# Define a function called login() which will have three parameters for:

#     username_attempt
#     password_attempt
#     profile

# If the values passed to the function for username_attempt and password_attempt match the values at the keys of username and password found in the profile, The login() function will return True.

# If the credentials don't match those in the profile, the login() function will return False

#     Create variables for a username_attempt and password_attempt which will emulate a user's login attempt.

#     Pass the profile dictionary, username_attempt and password_attempt to login(). Use the boolean that is returned to tell the user whether or not their login attempt was successful.

# Output:

# # successful login
# username: gandalfTheGrey
# password: noneShallPass!

# Welcome, gandalfTheGrey!

# # unsuccessful login
# username: gandalfTheGrey
# password: myPrecious?

# Error! Your username or password was incorrect!

# 5.2

# Create a REPL that asks the user for their username_attempt and password_attempt and attempts to log them in.

# If their login is successful, print a welcome message and end the program.

# If their login is unsuccessful, ask if they'd like to try again.
# 5.3

# Allow the user three attempts to login. If they exceed three attempts without a successful login, tell the user and end the program

# Output:

# username: gandalfTheGrey
# password: myPrecious?

# Error! Your username or password was incorrect!

# Enter 'y' to try again, 'n' to quit: y

# You have 2 login attempt(s) remaining...

# username: gandalfTheGrey
# password: foolOfATook!

# Error! Your username or password was incorrect!

# Enter 'y' to try again, 'n' to quit: y

# You have 1 login attempt(s) remaining...

# username: gandalfTheGrey
# password: bilboBaggins!

# Error! Your username or password was incorrect!

# Your login has been unsuccessful three times! Try again later. Goodbye!


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
