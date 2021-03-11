# https://github.com/PdxCodeGuild/Programming102/blob/master/labs/lab4.md
###############################################################################################################################################

welcome = 'Welcome to Anagram Checker v1.1. Now removes spaces!'
print(welcome)

user_string1 = input('Please enter your first word: ') #get the user's word
user_string1_mod = user_string1.lower() # make it lowercase
user_string1_mod = user_string1.replace(' ', '') # replace spaces with nothing
user_string1_mod = list(user_string1) # convert it to a list, without parameters, which makes each character a new list item
user_string1_mod.sort() # auto sort them, so alphabetically
# print(user_string1_mod) #just to check code working

user_string2 = input('Please enter your secand word: ') #get the user's word
user_string2_mod = user_string2.lower() # make it lowercase
user_string2_mod = user_string2_mod.replace(' ', '') # replace spaces with nothing
user_string2_mod = list(user_string2_mod) # convert it to a list, without parameters, which makes each character a new list item
user_string2_mod.sort()  # auto sort them, so alphabetically
# print(user_string2_mod) #just to check code working

def string_modifier():
    print(string_modifier)
    print('123')
    pass

string_modifier(input('Please enter your string modifier  word: '))


def main():
    if user_string1_mod == user_string2_mod:
        print(f'{user_string1} and {user_string2} are indeed anagrams!')
    else:
        print(f'Sorry, but {user_string1} and {user_string2} are not anagrams!')

main()

###############################################################################################################################################

    # Advanced Version 2

    # Make your program ignore punctuation when checking anagrams.

    # Advanced Version 3

    # Let the user enter as many words as they choose. If every word is an anagram of every other word, let the user know.