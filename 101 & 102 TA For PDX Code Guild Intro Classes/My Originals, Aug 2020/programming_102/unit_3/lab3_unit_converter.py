# This lab was a unit converter!
# @ https://github.com/PdxCodeGuild/Programming102/blob/master/labs/lab3.md
###############################################################################################################################################

units = {
    # LEGEND: 'unit_name':'distance_in_meters',
    'm':1, #meters
    'ft':0.3048, #feet
    'mi':1609.34, #miles
    'km':1000, #kilometers
    'yd':0.9144, #yards
    'in':0.0254, #inches
    }

welcome = 'Welcome to Unit Converter! Current output is always m. Inputs accepted: m, km, ft, mi, in, and yd'
print(welcome)

input_distance = input('Please enter the numerical distance, without units: ')
input_distance = float(input_distance)

input_conversion = input('Please enter your input units, exactly as written above: ')

# I don't just overwrite their input with the key value, because I want to print it soon...
conversion_factor = input_conversion
conversion_factor = units.get(conversion_factor, f'ERROR: Lookup of unit name {conversion_factor} failed...') # CHANGE

result = input_distance * conversion_factor
print(f'{input_distance} {input_conversion} = {result} m') 


# NEXT STEPS 1, make into a loop and keep asking
# NEXT STEPS 2 DO ADVANCED VERSION













###############################################################################################################################################

###############################################################################################################################################
# Lab 3: Unit Converter

# This lab will involve writing a program that allows the user 
# to convert a number between units.

# Version 1
# Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.

    # > what is the distance in feet? 12
    # > 12 ft is 3.6576 m

# Version 2
# Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers. Hint: Try using the unit as the key and the conversion as the value.

    # 1 ft is 0.3048 m
    # 1 mi is 1609.34 m
    # 1 m is 1 m
    # 1 km is 1000 m

# Below is some sample input/output:

    # > what is the distance? 100
    # > what are the units? mi
    # > 100 mi is 160934 m

# Version 3

# Add support for yards, and inches.

    # 1 yard is 0.9144 m
    # 1 inch is 0.0254 m
