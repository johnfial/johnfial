dividend = 10

divisor = input('enter a divisor: ')

try:
    divisor = float(divisor)
except ValueError:
    print(f'{divisor} cannot be converted to float!')
else:
    quotient = dividend / divisor
    print(quotient)

