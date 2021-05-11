def clock_angle_converter(input_time):
    '''
    Takes in min/hour and calculates the angle between them. 
    For now, assume that 090 = 270 is OK (it's the difference that matters, both of those are right angles).
    Also assume that the correct answer as > 360 or < 0 is also OK (for now!).
    '''

    hours = int(input_time[0:2])
    minutes = int(input_time[3:5])
    print(hours)

    # HOUR    # 360' and 12'
    hours_degrees = 360 / 12 * hours
        # FORGOT THIS!!!
        # 30 degrees per full hour...
        # increment the hour_degrees by % of minutes!
    increment_hours = (minutes / 60) * 30
    # print(f'~~~~~{increment_hours}')
    hours_degrees += increment_hours

    # MINUTES     # 360' and 60"
    minutes_degrees = 360 / 60 * minutes
    
    print(f'{hours}, {minutes}, {hours_degrees}, {minutes_degrees}')

    difference = hours_degrees - minutes_degrees
    
    # EXTRA
    # If negative, convert back (add 360), if > 360, minus 360

    print(difference)
    return difference

example_1 = '12:30'
example_2 = '06:00'
example_3 = '09:00'
example_4 = '01:45'

clock_angle_converter(example_2)


