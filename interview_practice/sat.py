def calc_drone_min_energy(route):
  
    # look at route[x[3]] then -1 unit energy or +1 for every integer diff

    battery_needed = 0
    current_height = route[0][2]

    for x in range(len(route)):
        print(current_height)

        current_height = route[x][2]

        if current_height <= route[x][2]:
            print('this')

    return battery_needed

  
  

route = [ [0,   2, 10],
            [3,   5,  0],
            [9,  20,  6],
            [10, 12, 15],
            [10, 10,  8] ]
# print(route[0][2])
calc_drone_min_energy(route)

#  Example:

# input:  route = [ [0,   2, 10],
#                   [3,   5,  0],
#                   [9,  20,  6],
#                   [10, 12, 15],
#                   [10, 10,  8] ]

# output: 5 # less than 5 kWh and the drone would crash before the finish
#           # line. More than `5` kWh and it’d end up with excess energy
