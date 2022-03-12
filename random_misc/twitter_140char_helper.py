# 2022 twitter helper, 
# A) BRUTE FORCE -- to take a string, break into 140-char segments, format output

# TODO
# B) break at the nearest word
# C) break at the nearest sensible English word (of, after, preposition list?)
# D) let user select where to break up (by index), then move to next segment

# figure out newlines


from numpy import string_


def break_into_140_characters(string):
    string_list = []
    print(f'string is {len(string)} characters')
    
    current = ''
    for i in range(len(string)):
        current += string[i]
        if len(current) == 140:
            current_temp = ''
            string_list.append(current)
            current = ''

    print(f'output string list is {string_list}')
    return string_list

example_string = '''
[F/S/G] All about them were small woods of resinous trees, fir and cedar and cypress, and other kinds unknown in the Shire, with wide glades among them; and everywhere there was a wealth of sweet-smelling herbs and shrubs. The long journey from Rivendell had brought them far south of their own land, but not until now in this more sheltered region had the hobbits felt the change of clime. Here Spring was already busy about them: fronds pierced moss and mould, larches were green-fingered, small flowers were opening in the turf, birds were singing. Ithilien, the garden of Gondor now desolate kept still a dishevelled dryad loveliness.	

[A/L/G/P] Aragorn rode to the Dike and watched till the king’s men were far down the Coomb. Then he turned to Halbarad. ‘There go three that I love, and the smallest not the least,’ he said. ‘He knows not to what end he rides; yet if he knew, he still would go on.’ ‘A little people, but of great worth are the Shire-folk,’ said Halbarad. ‘Little do they know of our long labour for the safekeeping of their borders, and yet I grudge it not.’ ‘And now our fates are woven together,’ said Aragorn. ‘And yet, alas! here we must part."

[Gand/P] ‘I wish I had known all this before,’ said Pippin. ‘I had no notion of what I was doing.’ ‘Oh yes, you had,’ said Gandalf. ‘You knew you were behaving wrongly and foolishly; and you told yourself so, though you did not listen. I did not tell you all this before, because it is only by musing on all that has happened that I have at last understood, even as we ride together. But if I had spoken sooner, it would not have lessened your desire, or made it easier to resist. On the contrary! No, the burned hand teaches best. After that advice about fire goes to the heart.’ ‘It does,’ said Pippin. ‘If all the seven stones were laid out before me now, I should shut my eyes and put my hands in my pockets.’
‘Good!’ said Gandalf. ‘That is what I hoped.’"
'''

break_into_140_characters(example_string)