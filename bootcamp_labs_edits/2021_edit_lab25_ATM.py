##############################################################################
# John Fial, PDX Code Guild, 2020-2021
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab25-ATM.md
##############################################################################
# ***************************** WORKING FROM HERE *****************************
# ***************************** ^^^^^^^^^ TO HERE *****************************

class ATM(): 

    def __init__(self, balance=0):        
        self.balance = balance
        self.history = []
        self.datetime = 'Today'
        self.history.append(f'Date: {self.datetime}. Account opened with starting balance of ${self.balance}.')

    def check_balance(self):
        print(f'Balance is ${self.balance}.')
        return self.balance
        
    def deposit(self,amount):
        # TODO REJECT STRING INPUT
        # TODO REJECT STRING INPUT
        # TODO REJECT STRING INPUT
        if amount <= 0:
            print(f'Invalid entry. Please use the withdrawl function to make a withdrawl. Balance is ${self.balance}.')
            return self.balance
        elif amount >0:
            self.balance += amount
            print(f'${amount} deposited. You new balance is ${self.balance}.')
            self.history.append(f'Date: {self.datetime}. Deposit: ${amount}. Balance is ${self.balance}.')
        else:
            print(f'Invalid input. Balance is ${self.balance}.')
        return self.balance

    def print_transactions(self):
        print('Beginning transaction history...')
        i = 1
        for item in self.history:
            print(f'{i}: {item}')
            i += 1
        print('...end of transaction history.')
    
    def check_withdrawl(self, amount):
        if self.balance > amount and amount > 0:
            return True
        else:
            return False
        print('invalid!')

    def withdraw(self,amount):

        self.check_withdrawl(amount)

        if self.check_withdrawl(amount) == True:
            self.balance -= amount
            print(f'${amount} withdrawn. You new balance is ${self.balance}.')
            self.history.append(f'Date: {self.datetime}. Withdrawl: ${amount}. Balance is ${self.balance}.')
            return self.balance
        else:
            self.history.append(f'Date: {self.datetime}. REJECTED Withdrawl for amount: ${amount}. Balance is ${self.balance}.')
            print(f'Sorry! Current balance is ${self.balance}; but you tried to withdraw ${amount}.')
            return self.balance

def next_operation():
    user_input = input(f'Enter next operation: ')    # user_input = 'create' # TEMP INPUT ### REMEMBER that invalid input here WILL LOOP, which is correct functionality!
    return user_input

def main(account):
    print('Welcome to ATM v1!')
    print(f'Acceptable operations are, without quotes: \"check balance\", \"deposit\", \"withdraw\", \"history\", \"menu\", or \"exit\": ')

    user_input = next_operation()

    while user_input != 'exit':
        if user_input == 'check balance':  
            account.check_balance() 
            user_input = next_operation()

        elif user_input == 'deposit':
            amount = input(f'Please enter the amount, as a number: ')
            try: 
                amount = float(amount)
                account.deposit(amount)
                user_input = next_operation()
            except ValueError:
                print('Invalid number. Please enter a valid number next time.')
                user_input = next_operation()
            # NOTE excellent lesson learned, as I originally had the .deposit and the next_opertation in the elif but OUTSIDE the try/except. 
            # NOTE Any error within the try statement will 'break' and jump to the except portion!

        elif user_input == 'withdraw':
            amount = input(f'Please enter the amount, as a number: ')
            try: 
                amount = float(amount)
                account.withdraw(amount)
                user_input = next_operation()
            except ValueError:
                print('Invalid number. Please enter a valid number next time.')
                user_input = next_operation()

        elif user_input == 'history':
            account.print_transactions()
            user_input = next_operation()

        elif user_input == 'menu' or user_input == 'help':
            print(f'Acceptable operations are, without quotes: \"check balance\", \"deposit\", \"withdraw\", \"history\", \"menu\", or \"exit\": ')
            user_input = next_operation()

        else: # for invalid input
            print('Invalid input!')
            user_input = next_operation()
            pass

    else: # if user_input is 'exit'...
        return 


##############################################################################

    # TESTING:
# account1.deposit(2)
# account1.deposit(-100)
# account1.deposit(2)
# # account1.print_transactions()
# # print(account1.check_withdrawl(-555))
# account1.withdraw(55)
# account1.withdraw(-55)
# account1.print_transactions()
# print(account1.balance) # NOTE this is where __str__ comes in useful or necessary


account1 = ATM(250)
account2 = ATM(5000)
# main(account1)


# TODO now can I make it use different accounts? Maybe with a username and password?



##############################################################################

print('     ~~~  PROGRAM ENDED  ~~~       ')
##############################################################################
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab25-ATM.md