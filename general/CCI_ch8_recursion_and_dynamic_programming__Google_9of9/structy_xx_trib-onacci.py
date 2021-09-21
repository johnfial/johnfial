trib_list = [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
# 30 TAKES A FEW SECONDS! 
trib_list_30 = [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513, 35890, 66012, 121415, 223317, 410744, 755476, 1389537, 2555757, 4700770, 8646064]
trib_list = []

def tribonacci(n):
    # WORKING:
    if n == 0:
      return 0
    if n == 1:
      return 0
    if n == 2:
      return 1

    return tribonacci(n-1) +  tribonacci(n-2) + tribonacci(n-3)

    # TODO memo-ize it...
    # try:
    #     if (trib_list[n]):
    #         return (trib_list[n])
    # except:
    #     new_num = tribonacci(n-1) +  tribonacci(n-2) + tribonacci(n-3)
    #     trib_list.append(new_num)
    # return new_num


for n in range(20):
    trib_list.append(tribonacci(n))

print(trib_list)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# TODO STATUS:    Working 2021 September...
# TODO SUBMITTED: No
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # #52 tribonacci
# https://structy.net/problems/tribonacci
# tribonacci

# Write a function tribonacci that takes in a number argument, n, and returns the n-th number of the Tribonacci sequence.

# The 0-th and 1-st numbers of the sequence are both 0.

# The 2-nd number of the sequence is 1.

# To generate further numbers of the sequence, calculate the sum of previous three numbers.

# Solve this recursively.
# test_00:

# tribonacci(0) # -> 0

# test_01:

# tribonacci(1) # -> 0

# test_02:

# tribonacci(2) # -> 1

# test_03:

# tribonacci(5) # -> 4

# test_04:

# tribonacci(7) # -> 13

# test_05:

# tribonacci(14) # -> 927

# test_06:

# tribonacci(20) # -> 35890

# test_07:

# tribonacci(37) # -> 1132436852