# use .capitalize or .title to capitalize
# use .swapcase method
# and .replace('old','new') might be useful too
# use /n for newlines today
# 

phrase = input('Please enter a word or phrase: ')

phrase_swapped = phrase.swapcase()
print(f'''
Thank you.
Calculating. . . . 
Just out of curiousity, when and where did you learn English?
Calculating. . . . 
Here's your input, but in a much more readable format for today's modern kompewtur: {phrase_swapped}
''')
