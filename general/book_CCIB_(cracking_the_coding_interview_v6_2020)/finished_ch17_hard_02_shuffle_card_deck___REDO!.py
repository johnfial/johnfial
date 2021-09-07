# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# http://www.crackingthecodinginterview.com/solutions.html 
# Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
# Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition
# TODO STATUS:      Finished

# TODO: Next challenge: sort the deck in place. How hard would that be?

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 17.2 Shuffle: Write a method to shuffle a deck of cards. It must be a perfect shuffle -- in other words, each
# of the 52! permutations of the deck has to be equally likely. Assume that you are given a random number generator 
# which is perfect.
# HINTS: 482, 578, 633


# 5 variables
cards_remaining = 52
deck_brand_new = [
                  'Ace of Clubs', 'Ace of Spades', 'Ace of Hearts', 'Ace of Diamonds', 
                  '02 of Clubs', '02 of Spades', '02 of Hearts', '02 of Diamonds', 
                  '03 of Clubs', '03 of Spades', '03 of Hearts', '03 of Diamonds', 
                  '04 of Clubs', '04 of Spades', '04 of Hearts', '04 of Diamonds', 
                  '05 of Clubs', '05 of Spades', '05 of Hearts', '05 of Diamonds', 
                  '06 of Clubs', '06 of Spades', '06 of Hearts', '06 of Diamonds', 
                  '07 of Clubs', '07 of Spades', '07 of Hearts', '07 of Diamonds', 
                  '08 of Clubs', '08 of Spades', '08 of Hearts', '08 of Diamonds', 
                  '09 of Clubs', '09 of Spades', '09 of Hearts', '09 of Diamonds', 
                  '10 of Clubs', '10 of Spades', '10 of Hearts', '10 of Diamonds', 
                  'Jack of Clubs', 'Jack of Spades', 'Jack of Hearts', 'Jack of Diamonds', 
                  'Queen of Clubs', 'Queen of Spades', 'Queen of Hearts', 'Queen of Diamonds', 
                  'King of Clubs', 'King of Spades', 'King of Hearts', 'King of Diamonds',
                  ]
deck_shuffled = []

import random
# WHITEBOARDED: Erroneously assumed I could use python's random module. No, I don't think that'd be allowed in an 
# interview -- but let's do the first version simply with it.
    # NOTE let's assume the random number generator gives us between 0-52. 
    # It's not a lot of work to make any random number (between 0-1 or 0-100000) convert to help pick
    # between 52 cards, but this is the easier step. Below was just using random.choice to choose 
    # the card for us, moved from within the while loop:
        # # OLD method using python's import random
        # # 7 pop a random card out
        # random_card = random.choice(deck_remaining_cards)
        # i = deck_remaining_cards.index(random_card)
        # deck_remaining_cards.pop(i)
        # deck_shuffled.append(random_card)


def shuffle_deck():
    
    # make a deck of the remaining cards (to shuffle), copied from the brand new deck
    deck_remaining_cards = deck_brand_new

    # 6 while cards_remaining
    while len(deck_remaining_cards) > 0:

        # 7 pop a random card out
        random_number = random.randint(0,len(deck_remaining_cards)-1)
        # print(f'random_number: {random_number}. len(deck_remaining_cards): {len(deck_remaining_cards)}.')  # helper print, bug was that the length wasn't len()-1, fixed above
        # pop the card off and append to the new deck        
        deck_shuffled.append(deck_remaining_cards.pop(random_number))  # baby steps, good on me: since list.pop() returns, we can return straight into the append method!
        # print(f'random_number: {random_number}. temp_card: {temp_card}. len(deck_remaining_cards): {len(deck_remaining_cards)}.')  # helper print
        

    print(deck_shuffled)

shuffle_deck()









# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # 1 make the deck -- list is ordered, so OK

# # 2 make a list of spades, clubs, etc...
# list_families = [
#     'Clubs',
#     'Spades',
#     'Hearts',
#     'Diamonds',
# ]

# # 3 make a list of numbers
# list_numbers = [
#     'Ace',
#     '02',
#     '03',
#     '04',
#     '05',
#     '06',
#     '07',
#     '08',
#     '09',
#     '10',
#     'Jack',
#     'Queen',
#     'King',
# ]

# # 4 make the permutations output, SAVE that as my list deck
# for card in list_numbers:
#     for family in list_families:
#         new_card = ''
#         new_card = card + ' of ' + family
#         print(new_card)
#         deck_brand_new.append(new_card)

# # 5 confirm len is 52
# print(deck_brand_new)
# print(len(deck_brand_new))






# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 