# merritt:pdxcodeguild:  10:50 AM
# Write a program that prints the numbers from 1 to 100. But for 
# multiples of three print “Fizz” instead of the number 
# and for the multiples of five print “Buzz”. 
# For numbers which are multiples of both three and five print “FizzBuzz”.

def fizzbuzz(input):
    for i in range(input):
        if i % 3 == 0 and i%5 == 0:
            print(f'fizzbuzz for i={i}!')
        elif i % 3 == 0:
            print(f'{i} is multiple of 3, i%3={i%3}')
        elif i % 5 == 0:
            print(f'{i} is multiple of 5, i%5={i%5}')
        else:

            print(i)

fizzbuzz(20)
# TIME FIRST TRY: ABOUT 5:15. Slow... I've seen the problem before but not sure I've ever written it
# Or it's been years...