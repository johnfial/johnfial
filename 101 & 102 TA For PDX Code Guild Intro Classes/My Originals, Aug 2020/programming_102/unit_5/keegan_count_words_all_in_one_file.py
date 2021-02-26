'''
Count Words
'''
from string import punctuation



def main():
    # Open text file
    with open('alice.txt', 'r') as text_file:
        # within this code block, the file is open
        
        # Read file contents as giant string
        dirty_text = text_file.read()

    # exit the file upon returning to this indentation
    

    # Clean the text - convert text to a giant list of lower case words.
    # remove new line characters (\n) replace with spaces
    clean_text = dirty_text.replace('\n', ' ')

    # remove punctuation - use string module punctuation variable
    # loop through each punctuation character and
    # replace it with a blank string
    for punct in punctuation:
        # overwrite the text with punct character removed
        clean_text = clean_text.replace(punct, '')

    # convert text to all lowercase
    clean_text = clean_text.lower()

    # split the text at the spaces to form a list
    word_list = clean_text.split(' ')
    

    # Count the occurances of the words in the list
    # Create a blank dictionary 
    # - keys will be the words, values will be their counts
    word_counts = {}

    # loop through the word list
    for word in word_list:
        # if the current word is NOT in the dictionary,
        if word not in word_counts:
            # add it with the starting value of 1
            word_counts[word] = 1

        # if the current word is already in the dictionary as a key,
        else:
            # add one to its value
            word_counts[word] += 1


    # sort the dictionary by value
    # take the first 10 items of the dictionary
    # these will be the most frequently occuring words
    
    # create a list of dict items
    words = list(word_counts.items())

    # sort the list of tuples by the value at index 1
    words.sort(key=lambda tup:tup[1], reverse=True)

    # create a list of the first ten items in the words list
    most_frequent_words = []
    for i in range(10):
        most_frequent_words.append(words[i])
    
    # convert list of tuples into dictionary
    most_frequent_words = dict(most_frequent_words)

    # write the 10 words and their counts a txt file
    # open a new txt file for writing
    with open('most_frequent_words.txt', 'w') as text_file:
        text_file.write('Most frequent words\n')
        text_file.write('-------------------\n')
        for word in most_frequent_words:
            count = most_frequent_words[word] # occurances of word
            text_file.write(f'{word} - {count}\n')

main()
