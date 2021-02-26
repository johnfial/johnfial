# This is a simple username/password login code.
# https://github.com/PdxCodeGuild/Programming102/blob/master/labs/user_login.md
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