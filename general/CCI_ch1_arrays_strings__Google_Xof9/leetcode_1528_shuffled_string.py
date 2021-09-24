# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# TODO STATUS:    Working 2021 September...
# TODO SUBMITTED: Yes, but poor runtime...
    # Runtime: 60 ms, faster than 41.29% of Python3 online submissions for Shuffle String.
    # Memory Usage: 14.3 MB, less than 54.03% of Python3 online submissions for Shuffle String.
# TODO improve...

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def shuffle_string(string, indices):
    output = ''

    # must be same length!
    if len(string) != len(indices):
        return None

    # 1 for x in range(indices)
    for x in range(len(indices)):
        output += string[indices.index(x)]
        
    print(output)
    return output


# Example 1:
shuffle_string("codeleet", [4,5,6,7,0,2,1,3])
# shuffle_string("codeleet", indices = [4,5,6,7,0,2,1,3])
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

# Example 2:

shuffle_string("abc", indices = [0,1,2])
# Output: "abc"
# Explanation: After shuffling, each character remains in its position.

# Example 3:

shuffle_string("aiohn", indices = [3,1,4,2,0])
# Output: "nihao"

# Example 4:

# Input: s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]
# Output: "arigatou"

# Example 5:

# Input: s = "art", indices = [1,0,2]
# Output: "rat"








# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 1528. Shuffle String
# Easy

# Given a string s and an integer array indices of the same length.

# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Return the shuffled string.

 


 

# Constraints:

#     s.length == indices.length == n
#     1 <= n <= 100
#     s contains only lower-case English letters.
#     0 <= indices[i] < n
#     All values of indices are unique (i.e. indices is a permutation of the integers from 0 to n - 1).

# Accepted
# 149,223
# Submissions
# 173,775