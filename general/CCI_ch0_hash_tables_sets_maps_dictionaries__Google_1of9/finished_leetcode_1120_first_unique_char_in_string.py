# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# by John Fial, 2021, https://github.com/johnfial/
# NOTE STATUS    : Started 2021 September
# TODO SUBMITTED : Yes, poor runtime/memory though...
# NOTE Concepts  :  
# - Hash Maps
# - 
# - 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def first_repeating_character_mistake(string):
    
    hash_set = set()
    
    for i in range(len(string)):
        if string[i] in hash_set:
            return i
        hash_set.add(string[i])

    return -1

def unique_char(string):

    charmap = {}
    for character in string:
        if character in charmap:
            charmap[character] = (charmap.get(character) +1 )
        else:
            charmap[character] = 1
    
    for i in range(len(string)):
        if charmap.get(string[i]) == 1:
            return i
    
    return -1

s = 'leetcode'
print(unique_char(s))

# s = 'loveleetcode'
# print(unique_char(s))

# s = 'aabb'
# print(unique_char(s))






# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1120/
# First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0

# Example 2:

# Input: s = "loveleetcode"
# Output: 2

# Example 3:

# Input: s = "aabb"
# Output: -1

 

# Constraints:

#     1 <= s.length <= 105
#     s consists of only lowercase English letters.

