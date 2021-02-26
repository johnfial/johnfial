# This lab was an Anagram Checker!
# https://github.com/PdxCodeGuild/Programming102/blob/master/labs/lab4.md
###############################################################################################################################################

def string_modifier(phrase):
    phrase = phrase.lower() # make it lowercase
    phrase = phrase.replace(' ', '') # replace spaces with nothing
    phrase = list(phrase) # convert it to a list, without parameters, which makes each character a new list item
    phrase.sort() # auto sort them, so alphabetically
    # print(user_string1_mod) #just to check code working
    return phrase

def main():

    welcome = 'Welcome to Anagram Checker v1.2. Now removes spaces! Now with hidden functions!'
    print(welcome)

    user_string1 = input('Please enter your first word or phrase, without punctuation: ')
    # user_string1 = 'aoeu5' # test

    user_string2 = input('Please enter your second word or phrase, without punctuation: ')
    # user_string2 = 'ao5e   u' # test
    
    input1 = string_modifier(user_string1)
    input2 = string_modifier(user_string2)

    if input1 == input2:
        print(f'{user_string1} and {user_string2} are indeed anagrams!')
    else:
        print(f'Sorry, but {user_string1} and {user_string2} are not anagrams!')

main()



###############################################################################################################################################

    # Advanced Version 2

    # Make your program ignore punctuation when checking anagrams.

    # Advanced Version 3

    # Let the user enter as many words as they choose. If every word is an anagram of every other word, let the user know.