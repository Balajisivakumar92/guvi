a=input('enter a number :')
b,e,c,d = a%10,a/10,e%10,e/10
x=b**3+c**3+d**3
if x==a:
    print "armstrong number"
else:
    print "not an armstrong number"
