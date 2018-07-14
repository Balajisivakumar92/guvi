import random
import collections

x = input('enter any number :')
q = []
for i in range(x):
    q.append(random.randint(1, x))
print q
print [i for i, count in collections.Counter(q).items() if count > 1]
