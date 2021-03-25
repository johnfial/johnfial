# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3260/
# TODO STATUS:
    # v1: yes/no all letters
    # v2: missing letters
    # v3: stats, length, # letters, dictionary
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


import string

letters = string.ascii_lowercase

def pangram_checker_yes_or_no(input_string):
    '''
    Pangram checker -- checks if a string/sentence contains each of our 26 letters of the alphabet.
    '''
    letters_seen_list = []
    letters_missing_list = []

    print(f'pangram_checker_yes_or_no() started with input_string > : \n"{input_string}"')
    modified_string = input_string.replace(' ', '').replace('.', '').lower() # 3 at once!
    
    for character in letters:
        if character in modified_string:
            letters_seen_list.append(character)
        else:
            letters_missing_list.append(character)
    
    if len(letters_seen_list) >= 26:
        # print(f'len(letters_seen_list): {len(letters_seen_list)}, which is >=26')
        print('Your string is a pangram; it *does* contain all 26 letters! Congratulations!')
        return True

    print(f'No, your string only contains {len(letters_seen_list)} letters. Missing: {letters_missing_list}. Try again!')
    return False

# words:
    # jabberwocky

# pangram_checker_yes_or_no(string1)
string1 = 'The quick brown fox jumps over the lazy dog.'

string2 = "The zany chamelion, victorious over the quacking fox, praised training with his jabberwocky!"
# pangram_checker_yes_or_no(string2)

string3 = "Here's a quick, zany sentence for bringing in the rain's swaying motion as it propels the cryptic karma through the universe!"
pangram_checker_yes_or_no(string3)

string4 = "Can John make it shorter, please, through quality or zoology, on our knees, poems swaying with candles, or cheese?"
# pangram_checker_yes_or_no(string4)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Spanish version with enya: 


# TODO make a word checker - suggester for a combination of letters remaining...
difficulty_medium = ['j', 'r', 'v', 'w', 'y',]
difficulty_hard = ['q', 'x', 'z']


# Test cases:


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Check If N and Its Double Exist



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   # 
#     #     #     #     #     #     #     #     #     #     #     #     #     #     #     #     #

























# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 