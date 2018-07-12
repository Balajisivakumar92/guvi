#ask the user for a number.depending on whether the number is even or odd
#print out an appropriate message to the user.

num = input('enter any number:')
mod = num % 2

if mod > 0:
    print 'you have entered odd number:',num
else:
    print 'you have entered even number:',num
    
