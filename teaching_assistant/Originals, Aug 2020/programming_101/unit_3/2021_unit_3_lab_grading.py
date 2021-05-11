# https://github.com/PdxCodeGuild/Programming101/blob/master/labs/grading.md
# if and elif statements
# input user_grade, then compare that user_grade to a randomint() of another student
# then output if they passed or not
import math
import random

def convert_numerical_to_letter_score(numerical_score):
    # print(f'function convert_numerical_to_letter_score() with input: {numerical_score}')

    numerical_score = int(numerical_score)

    if numerical_score == 100:
        letter_score = 'A+'
        return letter_score
    elif 90 <= numerical_score <= 99:
        letter_score = 'A'
    elif 80 <= numerical_score <= 89:
        letter_score = 'B'
    elif 70 <= numerical_score <= 79:
        letter_score = 'C'
    elif 60 <= numerical_score <= 69:
        letter_score = 'D'
    elif numerical_score <= 59:
        letter_score = 'F'
        return letter_score
    else:
        letter_score = 'input error'
        return letter_score

    appendix = ''
    if numerical_score % 10 <= 3:
        appendix = '-'
    elif numerical_score % 10 >=7:
        appendix = '+'
    else:
        appendix = ''

    letter_score += appendix
    return letter_score

def main():
    user_grade = input('''Please input your user_grade. 
    Remeber that falsifications are punishable by up to a $5000 fine and/or 2-years imprisonment.
    \nuser_grade> ''')
    # user_grade = 72  # testing
    user_grade = int(user_grade)

    if user_grade >= 90 and user_grade <= 100:
        user_statement = 'Congratulations, you must have studied hard!'
    elif user_grade >= 80 and user_grade <= 89:
        user_statement = 'Congratulations! Passing by all measures, but not to the point where you annoy any classmates!'
    elif user_grade >= 70 and user_grade <= 79:
        user_statement = '''Congratulations! You passed, and you\'re either dissapointed in yourself for the \'low\' score, or thrilled that you passed! 
    If the former, may I suggest you cheer up by spending more time with the underachievers *thrilled* with their \'Cs\'!'''
    elif user_grade >= 60 and user_grade <= 69:
        user_statement = 'Not much to see here, folks. . .'
    elif user_grade <= 59:
        user_statement = 'Wow. Bummer.'
    else:
        user_statement = 'input error'

    rival_score = random.randint(0,100)
    if user_grade > rival_score:
        rival_statement = 'Horray, you beat their score!'
    elif user_grade == rival_score:
        rival_statement = 'You tied their score -- exactly!'
    elif user_grade < rival_score:
        rival_statement = 'Unfortutately, you did not surpass their score.'

    final_output = f'''
    {user_grade}/100 is a {convert_numerical_to_letter_score(user_grade)}. {user_statement}
    With a {rival_score}/100, your rival scored a {convert_numerical_to_letter_score(rival_score)}. {rival_statement}    
    '''
    print(final_output)

main()