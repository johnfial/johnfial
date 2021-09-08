# 10.2 Group Anagrams: Write a method to sort an array of strings so that all the anagrams
# are next to each other.
# Hints: 177, 182, 263, 342
# NOTE STATUS: Currently grouping by length, not yet by anagram...

a = ['string', 'pony', 'four', 'furo', 'alphabet', 'ginrst', 'yopn', 'testing']

def group_anagrams(a):
    print(a)
    a.sort(key=len) # learned you can sort by key=len, cool! kinda cheating though? Unnecessary once I get the algorithm done?
    print(a)
    for i in range(len(a)):

        # testing
        if i == 0:
            # 1 string > list
            i_as_list = list(a[i])
            
            # 2 sort list
            i_as_list.sort()
            # print(i_as_list)
            
            # 3 list back to string
            i_as_list = ''.join(i_as_list)
            # print(i_as_list)
            
            # 4 change array at i?
            a[i] = i_as_list
            # print(a[i])
            # print(f'i={i}, a[i]={a[i]}, a[i]={a[i].sort()}')

    print(a)
    return a

group_anagrams(a)