

# 10.1 Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer 
# at the end to hold B. Write a method to merge B into A in sorted order.
# Hints: 332

list_a = [1, 2, 3, 4, 5, 6, 8, 22, 55, 90, ]
list_b = [1, 7, 8, 22, 56, 57, 89, 91, 999]

# must mean merge then sort, in otherwise the merged list must be combined, right?

def merge_sort(list1, list2):

    # merged = []
    # for a in list1:
    #     merged.append(a)
    # for b in list2:
    #     merged.append(b)
    # merged.sort()  # cheating

    for b in list2:
        for a in range(0, len(list1)): # go through list1, remember a is an index now!
            if b > list1[a]:
                pass
            elif b < list1[a]:
                list1.append(b)
            elif b == list1[a]:
                # list1.insert(a, b) # at index i, insert b (so after that item)
                pass



    print(list1)
    return list1

merge_sort(list_a, list_b)
