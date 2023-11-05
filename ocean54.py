def binary(L,p):#here we are defining a function 
    u=len(L)-1#len[1]-1
    l=0 
    
    while l<=u:#if the entered value is less than u  then returned by l+u//2 . 
         mid=(l+u)//2 
         #break the list in to two parts
         if L[mid]==p:
             return mid
         elif L[mid]<p:
             l=mid
         elif L[mid]>p:
             u=mid
             
L=[10,20,50,60,78,98,99]#provided list
p=60#provided number 

print(binary(L,p))