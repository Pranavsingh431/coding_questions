#define a function named sum which takes two values of two numbers and adds them.
def sum(a,b):
     c = a+b
     return c

#take input of the two numbers a and b for which the sum is to be calculated.
a = int(input("enter a number: "))
b = int(input("enter another number: "))

#print the sum of the numbers.
print(f"the sum of the given numbers is {sum(a,b)}")
