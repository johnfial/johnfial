# 10.6 Sort Big File: Imagine you have  a 20GB file with one string per line. Explain how you would sort the file. 
# Hints: 207

a = ['string', 'pony', 'four', 'furo', 'alphabet', 'ginrst', 'yopn', 'testing']

def sort_big_file(input):
    print(input)
    input.sort(key=len)
    print(input)
    for i in range(len(input)):
        if len(input[i]) == len(input[i+1]):
            print(f'inputs match @ i={i}, j=, input[i]={input[i]} input[i+1]={input[i+1]}')
    return input

sort_big_file(a)
# NOTE WHITEBOARDING:
# First breakup lines into strings inside array...
# sort array by length
# if len(string) == itself, sort by alphabetically?
# Hint: think about quick sort vs merge...