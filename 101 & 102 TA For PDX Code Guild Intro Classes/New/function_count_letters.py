# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# v1: yes/no all letters
# v2: missing letters
# v3: stats, length, # letters, dictionary
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


def all_alphabet_yes_or_no(input_string):
    '''
    Counts...
    '''
    characters_seen_list = []

    print(f'function() started with input_string: {input_string}')
    modified_string = input_string.replace(' ', '').replace('.', '').lower() # 3 at once!
    print(f'modified_string: {modified_string}')
    
    for character in modified_string:

        if character not in characters_seen_list:
            characters_seen_list.append(character)
    
    characters_seen_list.sort()
    print(characters_seen_list)
    print(len(characters_seen_list))

    if len(characters_seen_list) >= 26:
        print(f'len(characters_seen_list): {len(characters_seen_list)}, which is >=26')
        print('Your string DOES contain all 26 letters!')
        return True

    return False

string1 = 'The quick brown fox jumps over the lazy dog.'
string2 = 'The zany chamelion realized the quacking fox wanted to be a monkey shared his mother"s fierce apostlitic nation!'

tough_letters = 'Z and Q and Y and X and R'

print(all_alphabet_yes_or_no(string2))





# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 