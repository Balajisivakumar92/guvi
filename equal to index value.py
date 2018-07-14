#import random

def equal_index_value(n):
	s = []
	for i in range(0, len(n)):
		if i == n[i]:
			s.append(n[i])
	return s

x = input('enter any value :')
#a = []
#for i in range(x):
#    a.append(random.randint(0, x))
#print a

#print 'the output is :',equal_index_value(a)
print 'the output is :',equal_index_value(x)
