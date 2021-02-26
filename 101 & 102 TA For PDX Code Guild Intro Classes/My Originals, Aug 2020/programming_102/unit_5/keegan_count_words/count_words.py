'''
Count Words
'''

from helpers import (
    read_text_file,
    scrub_text,
    tally_words,
    most_frequent,
    write_to_file
)

def main():
    # read the text file
    dirty_text = read_text_file('alice.txt')

    # clean up the text and get a list of 
    # lower case words with no punctuation
    word_list = scrub_text(dirty_text)

    # count all the words into a dictionary
    word_counts = tally_words(word_list)

    # get the first ten items of the word counts dictionary
    most_frequent_words = most_frequent(word_counts)

    # write the most frequent words to a file
    write_to_file('most_frequent_words.txt', most_frequent_words)
    
main()
