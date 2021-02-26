# https://github.com/PdxCodeGuild/Programming101/blob/master/labs/magic-8-ball.md
# https://en.wikipedia.org/wiki/Magic_8-Ball

import random

answers = [
     'It is certain.',
     'It is decidedly so.',
     'Without a doubt.',
     'Yes – definitely.',
     'You may rely on it.',

     'As I see it, yes.',
     'Most likely.',
     'Outlook good.',
     'Yes.',
     'Signs point to yes.',

     'Reply hazy, try again.',
     'Ask again later.',
     'Better not tell you now.',
     'Cannot predict now.',
     'Concentrate and ask again.',

     'Don\'t count on it.',
     'My reply is no.',
     'My sources say no.',
     'Outlook not so good.',
     'Very doubtful.',
]

Ball_Answer = random.choice(answers)

print('Welcome to the digitized magic 8-Ball (TM}! Code Copyright C 2020 John Fial')

question = ''
if question == '':
    question = input('What is your question, human? It must be a yes/no question\n> ')
    print('Calculating. . .')
    print(ball_answer)
    again = input('Would you like to ask another question? \n Y\\N>')
# if again == Y:


