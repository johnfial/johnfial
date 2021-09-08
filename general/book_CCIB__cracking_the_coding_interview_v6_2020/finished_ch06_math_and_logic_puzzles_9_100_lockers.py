# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
    # http://www.crackingthecodinginterview.com/solutions.html 
    # Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
    # Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition
# TODO STATUS:    Finished 12 April
# TODO: Future... Could make them into discrete functions, give it different arguments...
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # 6.9 100 Lockers: 

# There are 100 lockers in a hallway. A man begins by opening all 100 lockers. 
# Next, he closes every 2nd locker. 
# Then, on his third pass, he toggles every 3rd locker.
# The process continues for 100 passes, so that on each pass i he toggles every i-th locker.
# After 100 passes in the hallway, when he only toggles locker #100, 
# how many lockers are open?

    # Hints: : 139, 172, 264, 306

# Extra: What if it continues for only n passes? (Safe to assume n <= 100? Would it matter?)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Variables
i = 1  # each pass, locker_num % i == 0, flip this locker number

max_lockers = 101 # 100 for realseys

lockers_dictionary = {
    # locker number : True OPEN, False CLOSED
    1: False,
    2: False,
    3: False,
    4: False,
    5: False,
    # below lockers 6-100, comment out for testing:
    6: False, 7: False, 8: False, 9: False, 10: False, 11: False, 12: False, 13: False, 14: False, 15: False, 16: False, 17: False, 18: False, 19: False, 20: False, 21: False, 22: False, 23: False, 24: False, 25: False, 26: False, 27: False, 28: False, 29: False, 30: False, 31: False, 32: False, 33: False, 34: False, 35: False, 36: False, 37: False, 38: False, 39: False, 40: False, 41: False, 42: False, 43: False, 44: False, 45: False, 46: False, 47: False, 48: False, 49: False, 50: False, 51: False, 52: False, 53: False, 54: False, 55: False, 56: False, 57: False, 58: False, 59: False, 60: False, 61: False, 62: False, 63: False, 64: False, 65: False, 66: False, 67: False, 68: False, 69: False, 70: False, 71: False, 72: False, 73: False, 74: False, 75: False, 76: False, 77: False, 78: False, 79: False, 80: False, 81: False, 82: False, 83: False, 84: False, 85: False, 86: False, 87: False, 88: False, 89: False, 90: False, 91: False, 92: False, 93: False, 94: False, 95: False, 96: False, 97: False, 98: False, 99: False, 100: False,
}

# main code
while i < max_lockers:

    print(f'~~~~~NEW PASS, PASS #{i} ~~~~~~')
    current_locker = 1  # ok to define this variable inside the outer loop
    while current_locker < max_lockers:
        
        if current_locker % i == 0:  # flip each relevant locker

            print(f'Pass {i}: Flipping current_locker: {current_locker}, new value: {lockers_dictionary[current_locker]}.')
            # Above is english, below is code:
            if lockers_dictionary[current_locker] == False:
                lockers_dictionary[current_locker] = True
            elif lockers_dictionary[current_locker] == True:
                lockers_dictionary[current_locker] = False
            # TODO is there a quicker way to 'flip' a boolean?
        
            else:  # this is just for testing:
                print('ERROR, WHY DID IT GO HERE?!?!?!')
                raise KeyError('wtf mate!')

        current_locker += 1  # increment the current locker:

    i += 1

# print the whole dictionary
print('final dictionary ' + f'{lockers_dictionary}')

# count the total open lockers
open_lockers = 0
for locker in lockers_dictionary:
    if lockers_dictionary[locker] == True:
        open_lockers += 1
print(f'Program ended. Out of {len(lockers_dictionary)} total lockers, there are now {open_lockers} open_lockers.')










# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 