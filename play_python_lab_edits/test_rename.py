# rename every .py file original_{filename}.py
# cycle

# import sys
# cycle through filename

# C:\-=Cloud=-\Sync\git\johnfial\johnfial\bootcamp_python_labs_originals

def main():
    filename = 'test.py'

    if '.py' in filename:
        filename = 'original_' + filename
        print(f'new filename: {filename}')
        return
    else:
        print(f'filename {filename} did not match')

main()



T = (24, 67, 34, 89, 56, 47, 26, 74)
max=T[0]
for x in T:
    if(x>max):
        max=x
print("maximum value is", max) 