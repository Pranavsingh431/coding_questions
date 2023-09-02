#using input function to enter a number.
x = int(input("enter a number: "))
#for loop is used to iterate any variable n from 2 to x+1.
for n in range(2, x+1):
#again for loop is used to get a series of numbers from 2 to n.
         for i in range(2, n):
#we are calculating the remainder when n divides i if the remainder is 0, it means it is not a prime number.             
             if (n%i)==0:
                  break
#but if the remainder is not 0, it is a prime number and it will display all the prime numbers in the range of n.              
         else:
            print(n)  
