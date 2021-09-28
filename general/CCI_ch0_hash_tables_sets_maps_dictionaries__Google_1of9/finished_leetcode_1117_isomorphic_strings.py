# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# TODO STATUS:    Working 2021 September...
# TODO SUBMITTED: yes
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Title

def isomorphic_check(s, t):
    if len(s) != len(t): return False

    pairs = {}

    for i in range(len(s)):

        if pairs.get(s[i]) == None:

            # if there's already a value for the target, reject the isomorphicism!
            if t[i] in pairs.values():  # NOTE this was bug on 4th check
                return False

            # otherwise add the key/value pair mapping
            pairs[s[i]] = t[i]

            # print(f'added key/value pair for i={i} : {[s[i]]} = {t[i]}')  # debug print

        elif pairs.get(s[i]) != t[i]:
            print('Falseeeee')
            return False
        print(pairs)  # debug print
    
    print('printing True')
    return True

# isomorphic_check('egg', 'add')
# isomorphic_check('foo', 'bar')
# isomorphic_check('paper', 'title')
isomorphic_check('badc', 'baba')  # FAIL, BUG fixed. see note on line ~22 'if t[i] in pairs.values()'




# https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1117/
# Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Example 1:

# Input: s = "egg", t = "add"
# Output: true

# Example 2:

# Input: s = "foo", t = "bar"
# Output: false

# Example 3:

# Input: s = "paper", t = "title"
# Output: true

 

# Constraints:

#     1 <= s.length <= 5 * 104
#     t.length == s.length
#     s and t consist of any valid ascii character.