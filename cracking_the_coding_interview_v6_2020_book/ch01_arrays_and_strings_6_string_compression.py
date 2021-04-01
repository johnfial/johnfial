# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
    # http://www.crackingthecodinginterview.com/solutions.html 
    # Amazon: https://www.amazon.com/Cracking-Coding-Interview-Gayle-McDowell/dp/0984782850/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=careercup-ctciwebsite-20&linkId=173f3d8878a1d7f0d131a85fbfc9f67f
    # Solutions GitHub: https://github.com/careercup/CtCI-6th-Edition
# TODO STATUS:    Started 1 April 2021
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 1.7 Rotate Matrix:
# Given an image represented by an N x N matrix, where each pixel in the image is represented by an integer, 
# write a method to rotate the image by 90 degrees. Can you do this in place?
    # Hints: 51, 100

    # My assumption-: go clockwise, doesn't matter.


def rotate_matrix(input_image):
    
    output_image = []

    # # # # # # # # # # # # # # # # # # # # # # # # # # 
    
    # BRAINSTORM...

    # I have no idea how to do this.
    # Was there a lab we built the paks and valleys? ____'- method was to have a loop within a loop for the x and y, and it was simple...
    
    # 1 create the input example... integer equals pixel...
    # so whole I might realistically have a file, i can just, for now, 'draw' a list of a grid of integers...
    # like this:
    example_1 = [
        [ 1, 2, 3, ],
        [ 4, 5, 6, ],
        [ 7, 8, 9, ],
        ]
    # which ideally would be rotated to:
    example_1_output_rotated = [
        [7, 4, 1, ],
        [8, 5, 2, ],
        [9, 6, 3, ],
        ]
    # So that's the goal for the output. Assume an easy 3x3 grid for now. 
    # 2 Then do what I did with my brain in code -- I took the first index of each of the three inner lists
    # But I took them in reverse, order, from "bottom" to "top" of the original image...
        # in reverse -1 steps of the original list, THEN put [0] of each list inside a new list, and set THAT to inner_list_1
        # then did the same thing, in reverse, for index [2]
        # so i'm using length of first inner list (or while len(output_image) len(input_image[0]))
    # # # # # # # # # # # # # # # # # # # # # # # # # # 
    
    for i in range(3):
        
        temp_list = []
        for c in range(3):
            temp_temp = input_image[i[c]]
            print(temp_temp)
            temp_list.append([input_image[c]])
# NOTE working here, working on getting an item from a list within a list... maybe search that?
        print(temp_list)
        output_image.append(temp_list)

    # print the output 'image' :
    line_num = 0
    for list_print in output_image:
        print(f'line {line_num} {list_print}')
        line_num += 1
        pass

    return output_image

example_1 = [   [ 1, 2, 3, ],
                [ 4, 5, 6, ],
                [ 7, 8, 9, ],
            ]
rotate_matrix(example_1)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# by John Fial, 2021, https://github.com/johnfial/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 