#enter a number.
n = int(input("enter a number: "))

#create an empty list.
l = []

define a and b as 0 and 1 as these are the first elements of fibonacci series.
a,b = 0,1

#iterate a variable named i upto n numbers.
for i in range(n):

#add an element a in the empty list l with each iteration.
     l.append(a)

#define new a and b as b and a+b because that's what happens in the fibonacci series.
     a,b = b,a+b

     
print(l)
