import inspect
def line_number():
    '''returns line number'''
    return inspect.currentframe().f_back.f_lineno
# print(f'line {line_number()}')

# 1 read file
file_to_open = 'day1.txt'
with open(file_to_open, 'r') as file:
    radar_data = file.read()

# 2 split each
radar_data_as_list = radar_data.split('\n')
# convert to integer
for x in range(0, len(radar_data_as_list)-1):
    radar_data_as_list[x] = int(radar_data_as_list[x])
radar_data_as_list.pop()
print(radar_data_as_list, len(radar_data_as_list))

# GOAL count the measurements larger than previous...
# https://adventofcode.com/2021/day/1
def count_measurements_part_one(input):
   
    differences_dict = {
        'increases': 0,
        'decreases': 0,
        'no change': 0,
    }

    # get first item
    previous = radar_data_as_list[0]

    # for each measurement...
    for x in range(1,len(radar_data_as_list)):
        
        # ...update current and prev
        current = radar_data_as_list[x]
        previous = radar_data_as_list[x-1]

        # 1 if current > previous, add to increases
        if current > previous:
            differences_dict['increases'] = differences_dict['increases'] + 1
        # 2 add to decreases
        elif current < previous:
            differences_dict['decreases'] = differences_dict['decreases'] + 1
        # else add to 'no change'
        elif current == previous:
            differences_dict['no change'] = differences_dict['no change'] + 1
        else:
            print('error!')
            return None

    print(differences_dict)
    return differences_dict['increases']

# print(count_measurements_part_one(radar_data_as_list))
print('*' * 20)

# https://adventofcode.com/2021/day/1#part2
def count_measurements_part_two(input):
    differences_dict = {
        'increases': 0,
        'decreases': 0,
        'no change': 0,
    }

    # get first item
    previous = radar_data_as_list[0]

    # for each measurement...
    for x in range(1,len(radar_data_as_list)):
        
        # IDEAS: make a dict with list index as the key, sum as the value?
        
        # ...update current and prev
        current = radar_data_as_list[x]
        previous = radar_data_as_list[x-1]

        # 1 if current > previous, add to increases
        if current > previous:
            differences_dict['increases'] = differences_dict['increases'] + 1
        # 2 add to decreases
        elif current < previous:
            differences_dict['decreases'] = differences_dict['decreases'] + 1
        # else add to 'no change'
        elif current == previous:
            differences_dict['no change'] = differences_dict['no change'] + 1
        else:
            print('error!')
            return None

    print(differences_dict)
    return differences_dict['increases']

print(count_measurements_part_two(radar_data_as_list))