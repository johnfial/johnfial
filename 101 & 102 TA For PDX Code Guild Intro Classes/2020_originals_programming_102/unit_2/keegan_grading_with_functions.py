import random

def get_score(student):
    '''calculate and return the student's score'''
    if student == 'user':
        score = input('Please enter your score 0-100: ')
        score = int(score)
    elif student == 'rival':
        score = random.randint(0,100)

    return score

def compare_score(user, rival):
    '''return the student that had the higher score'''
    if user > rival:
        message = 'You score higher than your rival!'
    elif user < rival:
        message = 'Your rival score higher than you!'
    elif rival == user:
        message = 'You tied your rival!'

    return message

def get_grade(score):
    '''
        Return a grade A-F based on the score
    '''
    if 90 <= score <= 100:
        grade = 'A'
    elif 80 <= score < 90:
        grade = 'B'
    elif 70 <= score < 80:
        grade = 'C'
    elif 60 <= score < 70:
        grade = 'D'
    elif score < 60:
        grade = 'F'

    return grade

def get_result(user_score, user_grade, rival_score, rival_grade):
    result = f'''
your score: {user_score}, your grade: {user_grade}
rival score: {rival_score}, rival grade: {rival_grade}
        '''
    
    return result

def main():
    # main body of the code
    
    # begin REPL
    while True:
        # generate scores for user and rival
        user_score = get_score('user')
        rival_score = get_score('rival') 
        
        # catch the results from get_grade() for user and rival
        user_grade = get_grade(user_score)
        rival_grade = get_grade(rival_score)

        # calculate the winner
        winner = compare_score(user_score, rival_score)

        # calculate the result
        result = get_result(user_score, user_grade, rival_score, rival_grade)

        # display the results
        print(result)
        print(winner)


        # Repeat the loop?
        again = input('Do you want to calculate another grade? y/n: ')

        # ensure the user enters either 'y' or 'n'
        while again not in ['y','n']:
            print('Invalid choice')
            again = input('Do you want to calculate another grade? y/n: ')

        if again == 'y':
            print("Okay! Let's go!")
            # repeat the loop
            continue
        elif again == 'n':
            print("Goodbye!")
            # end the loop
            break

main()