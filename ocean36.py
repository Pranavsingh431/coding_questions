n=int(input("enter the number of bins or ball"))
#here we are takin user input
l=[0]*n
#at first we are having empty list or having 0 balls in it
import random
for i in range (0,n):
    #from going 0,n
    a=random.randint(0,n-1)
    #we are taking any random bin
    l[a]+=1
    #adding 1 in ball in it

print (max (l))
#here we will get the max ball in a list