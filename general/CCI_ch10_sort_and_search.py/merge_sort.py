# so this is a two-pointer solution...
# using an extra array...
# i don't really like his solution, though... (or descriptions...)
# from https://www.youtube.com/watch?v=Mo4vesaut8g

import math

def merge_sort(array=list):
    if len(array) < 2:
        return array
    middle = math.floor(len(array) / 2)
    left = array[0 : middle]
    right = array[middle:]
    print(left, right)

    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    result = []

    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    print(f'result array {result}')
    return result

list1 = [1, 5, 9, 8, 4, 3, 8, 5, 2222, 8, 9, 11, 84, 74 ]
print(merge_sort(list1))