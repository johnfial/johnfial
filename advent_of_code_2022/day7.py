# https://adventofcode.com/2022/day/7
# Part 1: ____
# Part 2: ____

'''--- Day 7: No Space Left On Device ---
You can hear birds chirping and raindrops hitting leaves as the expedition proceeds. Occasionally, you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?

The device the Elves gave you has problems with more than just its communication system. You try to run a system update:

$ system-update --please --pretty-please-with-sugar-on-top
Error: No space left on device
Perhaps you can delete some files to make space for the update?

You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input). For example:

$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called /. You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.

Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:

cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
cd / switches the current directory to the outermost directory, /.
ls means list. It prints out all of the files and directories immediately contained by the current directory:
123 abc means that the current directory contains a file named abc with size 123.
dir xyz means that the current directory contains a directory named xyz.
Given the commands and output in the example above, you can determine that the filesystem looks visually like this:

- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
Here, there are four directories: / (the outermost directory), a and d (which are in /), and e (which is in a). These directories also contain files of various sizes.

Since the disk is full, your first step should probably be to find directories that are good candidates for deletion. To do this, you need to determine the total size of each directory. The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)

The total sizes of the directories above can be found as follows:

The total size of directory e is 584 because it contains a single file i of size 584 and no other directories.
The directory a has total size 94853 because it contains files f (size 29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a contains e which contains i).
Directory d has total size 24933642.
As the outermost directory, / contains every file. Its total size is 48381165, the sum of the size of every file.
To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)

Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?'''

ex1_string = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

ex1_io = ex1_string.split('\n')

# actual part 1
file_to_open = 'day7.txt'
with open(file_to_open, 'r') as file:
    day7_part1 = file.read()

day7_io = day7_part1.split('\n')

# print(type(ex1_io), len(ex1_io), ex1_io[:5])
print(type(day7_io), len(day7_io), day7_io[:10])

# brute #1, almost certainly will be way too high with duplicate files:
# brute: get file size from each line with a file -- breaks if any commands/lines start with integers
def brute_force(input_commands):
    size = 0
    counter =0

    # loop over every line
    for line in input_commands:
        counter += 1

        # if the first char is an int (easier to do keeping it strings)...
        if line[0] in '0123456789':
            # ... split the size and filename, add size to total
            parsing = line.split(' ')
            size += int(parsing[0])
        
    print(f'counter of lines in input = {counter}')
    return size

# print(brute_force(ex1_io))
# 48,381,165 (example brute force) -- correct for example

# print(brute_force(day7_io)) 
# 44,965,705 (actual brute force) too high

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# PART 1 -

def find_size(input_commands):
    size = 0
    pwd = ''
    counter = 0
    file_tree = {'/': 0,}

    # TODO # change from per line to two pointer approach?

    for line in input_commands:
        print(f'   >>>> {counter} <<<< counter, current $PWD = {pwd}, line/command = `{line}`')
        counter += 1
            
        if counter == 20: break

        # if it's cd, change PWD variable
        if line[0:4] == '$ cd':
            ignore1, ignore2, destination = line.split(' ') 
            # print(ignore1, '***', ignore2, destination)

            if destination == '..':

                
                # find the LAST '/' by working in reverse
                index = pwd[::-1].find('/')
                
                # print(f'current PWD = {pwd}')
                # print(pwd[::-1])
                # print(index)
                
                #new $PWD is previous by chopping off until the end '/'
                pwd = pwd[ :: index+1 ]
                print(f'current PWD changed to = {pwd}')
                continue
            
            # else:
            pwd += destination
            print(f'current PWD changed to = {pwd}')

        # if it's a file, it starts with an integer, so count it, add its path:size to dict, and sum its size to its parent
        if line[0] in '0123456789':
            size, file = line.split(' ')
            size = int(size)
            
            # add the PWD for a unique key
            file = pwd + file
            
            if file in file_tree: 
                print(f'PASSING already seen files {file} !')
                continue
            
            print(f'file {file} is size {size}, adding to file_tree')

            # add the filesize with path as unique key
            file_tree[file] = size

            # WORKING HERE !!! NOTE TODO ???  
            # NOTE this only does this for ONE parent... best way to do it for EACH parent dir? Or sum up all at end somehow?
            # ... or actually use a tree?

            # chop off ../ and add size to parent!
            index = pwd[::-1].find('/')
            parent = pwd[ :: index+1 ]
            print(parent)
            print(index, type(parent), parent, file_tree.get(parent))
            
            try: # if parent dir exists...
                parent_size = file_tree.get(parent)
                file_tree[parent] = (parent_size + size)

            except: # ... no parent dir exists yet
                file_tree[parent] = size

            print(f'line ~209 parent_size = {parent_size} | file_tree[parent] = {file_tree[parent]} ')
        

        # TODO dir output ??
        if line[0:3] == 'dir':
            dir_type, name = line.split(' ')
            # print('dir commnd >>>>>', dir_type, name, '*********')
            # TODO: add PWD to file list so parent exists?

        # # TODO ls command... skip?
        # if line[0:2] == 'ls':
        #     continue

    print(file_tree)
    # END function()
    return file_tree['/']

print(find_size(day7_io))

# BRAINSTORM:

# HOW TO create a map for paths... # do I need a tree/trie?
# for each file, lookup its path. create a new path
#  make a PWD that sets the working dir based on $ cd... and $ cd .. commands. adding or chopping from the PWd string...
# for each file (starts with number), lookup if its path exists in the file_tree {} dict. If yes, skip, otherwise add its path as key and size as value
  # also add its size to the size of all parent directories (this would be by adding to each )

# ^ breaks if 'ls' is repeated in any directory...


# count from "$ ls" through to next /n 
# split all into commands
# parse commands:
  # put all directory lines into tree IF don't exist, as children
  # put all files and sizes, IF don't exist, as a dict pair