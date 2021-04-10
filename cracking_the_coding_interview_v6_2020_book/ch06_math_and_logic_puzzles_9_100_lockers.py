# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
    # http://www.crackingthecodinginterview.com/solutions.html 
    # Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
    # Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition
# TODO STATUS:    Created 09 April
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

i = 1  # each pass, locker_num % i == 0, flip this locker number

max_lockers = 16 # 100 for realseys

lockers_dictionary = {
    # locker number : True OPEN, False CLOSED
    1: False,
    2: False,
    3: False,
    4: True,
    5: False,
}

while i < max_lockers:
    current_locker = 1
    while current_locker < max_lockers:
        # flip each relevant locker
        if current_locker % i == 0:
            print(f'current_locker: {current_locker} needs to be flipped on this pass, pass {i}')
            # change the dictionary entry...

        # increment the current locker:
        current_locker += 1
    print('~~~~~new pass~~~~~~')
    i += 1






# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 