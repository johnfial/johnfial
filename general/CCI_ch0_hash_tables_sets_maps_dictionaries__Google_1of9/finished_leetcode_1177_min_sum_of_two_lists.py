# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# TODO STATUS:    Working 2021 September...
# TODO SUBMITTED: Technically fail test 4 (current line 44 below, but seems fine to me, their output is wierd...)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 1177 Minimum Index Sum of Two Lists

def common_restaurants(list1, list2):
    def fail_for_no_index():
        # TODO 1 input strings from list1 into hash set
        set1 = set(list1)

        # TODO 2 for each string in list 2, IF IT'S IN hash set, add to output list
        common = list(set1.intersection(set(list2)))
        
        # TODO 5 return list
        print(common)
    
    common = []
    dict1 = {}

    for restaurant in list1:
        if restaurant in list2:
            dict1[restaurant] = list1.index(restaurant)
    
    for restaurant in list2:
        if restaurant in dict1.keys():
            dict1[restaurant] = (dict1.get(restaurant) + list2.index(restaurant))
            # print(f'{restaurant} : {dict1[restaurant]} = ({dict1.get(restaurant)} + {list2.index(restaurant)})')  # debug print

    min = (float('inf'))
    for key, value in dict1.items():
        # print(key, value)
        if value < min:
            min = value
        common.insert(value, key)
    
    print(common[0])
    return common[0]

# common_restaurants(["Shogun","Tapioca Express","Burger King","KFC"],["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"])
# common_restaurants(["Shogun","Tapioca Express","Burger King","KFC"],["KFC","Shogun","Burger King"])
common_restaurants(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]) # Expected: ["Shogun"]
# Output: ["S","h","o","g","u","n"]
# Expected: ["Shogun"]



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1177/
# Minimum Index Sum of Two Lists

# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

# Example 1:

# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".

# Example 2:

# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

# Example 3:

# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
# Output: ["KFC","Burger King","Tapioca Express","Shogun"]

# Example 4:

# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
# Output: ["KFC","Burger King","Tapioca Express","Shogun"]

# Example 5:

# Input: list1 = ["KFC"], list2 = ["KFC"]
# Output: ["KFC"]

 

# Constraints:

#     1 <= list1.length, list2.length <= 1000
#     1 <= list1[i].length, list2[i].length <= 30
#     list1[i] and list2[i] consist of spaces ' ' and English letters.
#     All the stings of list1 are unique.
#     All the stings of list2 are unique.