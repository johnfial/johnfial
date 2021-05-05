"""

Author: Jeremy Bush
Project: Programming 102, Lab 2
Version: 1.0
Date: 5/4/2021

"""


# Define function to add numbers together
def sum_numbers(num_list):
    total = 0
    for number in num_list:
        total += int(number)

    return total


# Define function to remove a number from passed list
def remove_all(numbers, target):
    new_list = [number for number in numbers if number != target]
    return new_list


# Get user input
user_nums = []

print(" Add Some Numbers ".center(36, "*"))
while True:
    choice = 0
    choice = input("Please enter an integer, or 'done' to continue: ")

    # Check choice to see if it == done
    if choice == 'done':
        print(f"You entered {user_nums}")
        print(f"The total of the numbers you entered is: {sum_numbers(user_nums)}")
        break
    else:
        user_nums.append(int(choice))

# Reset the value of choice and get number to remove from list.
choice = input("Please enter a number to remove: ")

altered_list = remove_all(user_nums, choice)

print(f"Target: {choice}")
print(f"Updated List: {altered_list}")
