'''
this is used to add a comment line
or a set of lines that the computer ignores
'''
# this is used to add a single comment line

print("this is used to" + " concatenate 2 strings")

'''
a string and a number cannot be concatenated this way
instead we can use a comma to separate the two different data types'''

print(9, ' aousnik')

#BREAK AND CONTINUE::

magicNumber = 26
for x in range(101):
    if x is magicNumber:
        print(x," is a magic number")
        #once 26 is found it prints the number and breaks the loop
        break
    else:
        print(x)
        #prints the number anyways

'''numbers till 100 divisibe by 4'''

print('\n')

for i in range(1, 101):
    x = i%4
    if x is 0:
        print(i)