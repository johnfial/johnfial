# GOAL count the measurements larger than previous...


import inspect
def line_number():
    '''returns line number'''
    return inspect.currentframe().f_back.f_lineno

# read file
file_to_open = 'day1.txt'
with open(file_to_open, 'r') as file:
    radar_data = file.read()

# split each
radar_data_as_list = radar_data.split('\n')
# convert to integer
for x in range(0, len(radar_data_as_list)-1):
    radar_data_as_list[x] = int(radar_data_as_list[x])
radar_data_as_list.pop()
print(radar_data_as_list, len(radar_data_as_list))

def count_measurements(input):
    count = 0
    # print(f'line {line_number()}')
    

    # for each measurement...
    for measure in radar_data_as_list:
        previous = 0
        previous = measure
        return
    # if it's the first, don't count it
    # track previous
    # track current
    # if current > previous, add increase counter

    return count

data = [0]
print(count_measurements(radar_data_as_list))

# print(radar_data_as_list)
