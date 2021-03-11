# Original:
#  print 'The last letter of 'elephant' is: {'elephant'[8]}')
# https://github.com/PdxCodeGuild/Programming102/blob/master/practice/unit_1/exercise_3.md


elephant = 'elephant'
print(f'The last letter of \'elephant\' is: {elephant[7]}') # was out of range, indexing starts at #0 !!


# troubleshooting breaking it down:
# had to define string
# elephant = 'elephanteeeee'
# print(elephant[3])
