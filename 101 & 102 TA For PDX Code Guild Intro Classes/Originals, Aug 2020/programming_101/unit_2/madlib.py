'''
Example Mad Lib:
Date: _______

NAME is sick
with the PART OF BODY flu.
Drink more TYPE OF FLUID and
take SUBSTANCE as needed.

SIGNED: //PDXCODEGUILD101
'''

# randomized following for more fun
fluid = input('Input a healing fluid: ')
date = input('Input the *official* date: ')
body_part = input('Input a body part: ')
name = input('Input the student name: ')
substance = input('Input a powerful substance: ')

# puts the string together here
madlib = f'''
-----------------
Date: {date}

Dear teacher,

{name} is sick with the {body_part} flu.
Ensure student drinks more {fluid} and takes {substance} as needed.

Sincerely,

SIGNED: //PDXCODEGUILD101ADMIN
-----------------
'''

#prints the full string/message
print(madlib)
