print('hi manya here is your calculator')
i=int(input('enter first number: '))
j=int(input('enter second number: '))
choice = input('Enter your choice (add, sub, mul, div): ')
def added(i,j):
    return i+j

def subracted(i,j):
    return i-j

def multiplied(i,j):
    return i*j

def divided(i,j):
    return i/j

if choice=='add':
    print( added(i, j ))
    exit()
elif choice=='sub':
    print(subracted(i, j )) 
    exit() 
elif choice=='mul':
    print(multiplied(i, j ))
    exit()
elif choice=='div':
    print(divided(i, j ))
    exit()
else:
    print('Invalid choice, please try again.')

print('This is the end of the program.')