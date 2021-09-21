def merge_sort(list1, list2):

    # NOTE can I use .insert?
    index1 = len(list1)-1
    index2 = len(list2)-1
    index_merged = 0 ## NOTE

    while len(list2) > 0:
        # NOTE TODO BS:
        # 1 
        if index1 >= 0 and list1[index1] > list2[index2]:
            print('this is bigger!')
            break
        break
    
        # 332 hint: try moving from the end of the array to the beginning

    def ignore():
        for b in list2:
            for a in range(0, len(list1)): # go through list1, remember a is an index now!
                if b > list1[a]:
                    pass
                elif b < list1[a]:
                    list1.append(b)
                elif b == list1[a]:
                    list1.insert(a, b) # at index i, insert b (so after that item)
                    pass



    print(list1)
    return list1

list_a = [1, 2, 3, 4, 5, 6, 8, 22, 55, 90, ]
list_b = [1, 7, 8, 22, 56, 57, 89, 91, 999]

merge_sort(list_a, list_b)

# 10.1 Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer 
# at the end to hold B. Write a method to merge B into A in sorted order.

# Hints: 332

# must mean merge then sort, in otherwise the merged list must be combined, right?