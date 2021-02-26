# FUNctions!
'''
Functions

- are named blocks of code
- they run only when called upon
- typically designed to perform a singular task
    - may consist of multiple steps, but usually just one overall goal
- once defined, you can call them as many times as needed
- are like variables that store blocks of code
'''

# define a function with the keyword:
# def

'''
def function_name(parameters):
    # this code block
    # is run when the function
    # is called

    # the parameter data was changed somehow
    result = manipulated_parameters 

    return result

# 'call' the function
function_name(arguments)
'''

'''
def display_message(message):
    print(message)

# call display_message()
display_message('Hello world!')
display_message("I don't like spam!") 
'''


'''
def punctuate(text, punctuation):

    # print('text: ', text)
    # print('punctuation: ', punctuation)

    # concatenate the punctuation onto the text
    punctuated_text = text + punctuation 
    
    # this will be returned to wherever the function was called
    return punctuated_text

    # if no return value is specified, the function
    # will return None by default

result = punctuate('Hello world', '!')
print(result)

result = punctuate("I don't like spam", '?')
print(result)
'''



# the parameter n has a default value of 1
# which will be overwritten if a value is passed for it
def power_n(number=2, n=1):
    '''
        Return number to the power of n
    '''
    return number ** n

print(power_n(10, 2)) # 100 - overwrite the default value for n
print(power_n(15)) # 15 - default value for n is used
print(power_n()) # 2 - both parameter defaults are used

print(power_n(n=10)) # 1024 - 'keyword' arguments can specify values for certain parameters
print(power_n(n=10, number=6)) # 60466176 - keyword arguments can be in any order





#             param:type, param:type
def punctuate(text:str, punct:str):
    '''
        DOCSTRING provides description of the function

        Return the concatenation of text and punct
    '''
    return text + punct

# punctuate('hello','!')
