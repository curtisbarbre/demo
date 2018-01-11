import random, math, sys, os
# use: from random import *.
# to import library without need to use random.function()...etc

spam = 0
while not spam > 5:
    print('Hello, world.')
    spam = spam + 1

def hello(name):
    if name =='curtis':
        print('welcome curtis')
        return 'curtis'
    elif name =='c':
        print('initial')
        global spam
        spam = 10
        return 'curtis' #return exits the func. must be after change to global spam, which must be declared bfore can be changed by the func..
    elif myName == 'exit':
        #using myName as global variable since it's not a parameter of the func or defined local to the func
        sys.exit()
    else:
        print('hi stranger')
        return name
    
# use break and continue commands

print('What is your name?')
    
myName = input()

myName = hello(myName)
print('spam =', str(spam))

print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))

print('What is your age?')    # ask for their age
myAge = input()
try:
    print('You will be ' + str(int(myAge) + 1) + ' in a year.')
except ValueError:
    print('not a number')

print(bool(1 or 0))
print(not bool(1 or 0))
    
for i in range(12, 26, 2):
    print(i)
    
#runs the starting condition, breaks on the  stopping condition without executing that time
#(starting, stopping, stepping)
for i in range(5, -1, -1):
    print(i)
    print(random.randint(10,20))
    
spam = print ('smap')
spam == None
#data with None datatype. could be useful

print('cats', 'dogs', 'mice', sep=',')
print('cats', 'dogs', 'mice')