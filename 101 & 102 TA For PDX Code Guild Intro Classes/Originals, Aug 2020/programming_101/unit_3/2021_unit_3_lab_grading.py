# https://github.com/PdxCodeGuild/Programming101/blob/master/labs/grading.md
# if and elif statements
# input grade, then compare that grade to a randomint() of another student
# then output if they passed or not
import math
import random

def main():
    # grade = input('''Please input your grade. 
    # Remeber that falsifications are punishable by up to a $5000 fine and/or 2-years imprisonment.
    # \nGrade> ''')
    grade = 75

    grade = int(grade)
    if grade >= 90 and grade <= 100:
        print('Congratulations, you received an \'A\'! You must have studied hard!')
    elif grade >= 80 and grade <= 89:
        print('Congratulations, you received a \'B\'! Passing by all measures, but not to the point where you annoy any classmates!')
    elif grade >= 70 and grade <= 79:
        print('''
        Congratulations, you received a \'C\'! 
        You passed, and you\'re either dissapointed in yourself for the \'low\' score, 
        or thrilled that you passed! If the former, may I suggest you cheer up by 
        spending more time with the underachievers *thrilled* with their \'Cs\'!''')
    elif grade >= 60 and grade <= 69:
        print('You received a \'D\'. Not much to see here, folks. . .')
    elif grade <= 59:
        print('Wow, you received an \'F\'. Bummer.')
    else:
        print('input error')

    rival_score = random.randint(0,100)
    if grade > rival_score:
        print(f'An anonymous rival scored a {rival_score}. Horray, you beat their score!')
    elif grade == rival_score:
        print(f'An anonymous rival scored a {rival_score}. You tied their score -- exactly!')
    elif grade < rival_score:
        print(f'An anonymous rival scored a {rival_score}. Unfortutately, you did not surpass their score.')

    rival_appendix = ''
    if rival_score % 10 <= 3:
        rival_appendix = '-'
    elif rival_score % 10 >=7:
        rival_appendix = '+'

    final_output = f'''
    {rival_appendix}
    '''
    # BUG  100 printed wrong!
    print(final_output)

main()