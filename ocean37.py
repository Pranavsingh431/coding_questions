n=int(input("enter the number of bins"))
#input user
l=[0]*n
#taking list or balls in bins as 0 at first
c=0
#at first ballis 0
import random
while 0 in l: 
    #while ball is 0
    a=random.randint(0,n-1)
    #we are taking any random bin
    l[a]+=1
    #throw ball add a ball in list
    #adding 1 in ball in it
    c=c+1
    #and count it as a ball
print(c)
#print the numbers of  balls 