x,z = input('enter a number :')
print("Prime numbers between",x,"and",z,"are:")
a = range(x,z)
b = a[:-1]
c = a[1:]
for num in c:
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
