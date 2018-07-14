import random
import numpy as np

x = input('enter any number :')
c = []
for i in range(x):
    c.append(random.randint(0, x))
print c
d = sorted(c , key = int , reverse = True)
print 'largest number in the order :',np.array(d)


