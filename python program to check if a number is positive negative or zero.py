# python program to check if a number is positive negative or zero #

a = int(input("enter the number you need to check for +ve and -ve and 0 :")) # give a input that you need to check positive number or negative number or its zero
if a > 10000: # this is condition for input size
    print 'enter the number between 100000.That you entered number is invalid' # print if input is greater then input size
elif a < -10000: # this is condition for input size
    print 'enter the number between -100000.That you entered number is invalid' # print if input is lesser then input size
elif a > 0: # condition for positive number
    print 'number is positive'
elif a == 0: # condition for zero 
    print 'number is zero'
else: # condition for negative number
    print 'number is negative'
	
