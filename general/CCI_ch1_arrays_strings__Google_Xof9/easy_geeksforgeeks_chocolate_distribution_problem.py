# # # # # # # # # # # # # # # # # # # # #u # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# http://www.crackingthecodinginterview.com/solutions.html 
# Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
# Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition
# TODO STATUS:    Started 22 September
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import math

def distribute_chocolate(packets_list, students):
    
    # TODO 1 sort list
    packets_list.sort()
    
    # TODO 2 add m elements to a list
    # TODO 3 calculate the max() and min() of those, then calculate difference; STORE THAT variable
    # TODO 4 repeat for each combination while i + m < len(packets_list)
    # TODO return min of those differences... ideally, too, store WHERE (which sequence 
    # of student #s of packets) that group of packets was from

    compare_list = []
    try:
        for i in range(students):
            compare_list.append(packets_list[i])
        print(compare_list)
    except: pass

    return packets_list

distribute_chocolate([7, 3, 2, 4, 9, 12, 56,],3)
distribute_chocolate([3, 4, 1, 9, 56, 7, 9, 12,],5)
distribute_chocolate([12, 4, 7, 9, 2, 23, 25, 41, 
30, 40, 28, 42, 30, 44, 48, 
43, 50,],7)



# https://www.geeksforgeeks.org/chocolate-distribution-problem/
# Chocolate Distribution Problem

#     Difficulty Level : Easy
#     Last Updated : 22 Apr, 2021

# Given an array of n integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 

#     Each student gets one packet.
#     The difference between the number of chocolates in the packet with maximum chocolates and packet with minimum chocolates given to the students is minimum.

# Examples:

#     Input : arr[] = {7, 3, 2, 4, 9, 12, 56} , m = 3 
#     Output: Minimum Difference is 2 
#     Explanation:
#     We have seven packets of chocolates and 
#     we need to pick three packets for 3 students 
#     If we pick 2, 3 and 4, we get the minimum 
#     difference between maximum and minimum packet 
#     sizes.

#     Input : arr[] = {3, 4, 1, 9, 56, 7, 9, 12} , m = 5 
#     Output: Minimum Difference is 6 
#     Explanation:
#     The set goes like 3,4,7,9,9 and the output 
#     is 9-3 = 6

#     Input : arr[] = {12, 4, 7, 9, 2, 23, 25, 41, 
#     30, 40, 28, 42, 30, 44, 48, 
#     43, 50} , m = 7 
#     Output: Minimum Difference is 10 
#     Explanation:
#     We need to pick 7 packets. We pick 40, 41, 
#     42, 44, 48, 43 and 50 to minimize difference 
#     between maximum and minimum. 