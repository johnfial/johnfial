# https://adventofcode.com/2021/day/2

# 1 input and modify file
file_to_open = 'day2.txt'
with open(file_to_open, 'r') as file:
    input = file.read()

input_modified = input.split('\n')
# for x in range(0, len(input_modified)-1):
#     input_modified[x] = int(input_modified[x])
# input_modified.pop()
print(input_modified, len(input_modified))

# https://adventofcode.com/2021/day/2
def dive_ship(movements):
    print(movements)
    return 

print(dive_ship(input_modified))
print('*' * 20)
