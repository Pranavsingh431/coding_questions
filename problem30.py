#define a function named gcd to find the gcd of two numbers a and b.
def gcd(a,b):
#for the given values of a and b using while loop till b is not equal to o and redefining a and b as b and a mod b because that is what is in the euclid's algorithm.
   while b!=0:
        a,b = b,a%b
#this implies that the a in the last step will be the gcd of the given two numbers.
   return a

#take the input of a variable named k which is the number of digits for two numbers for which the gcd is to be calculated.
k = int(input("enter the value of k: "))

#define two variables max and max_pairs both with nothing in them.
max = 0
max_pairs = None

#using for loop to iterate i and j for given range which depends on k by the following expression:
for i in range(10**(k-1),10**k):
        for j in range(10**(k-1),10**k):

#define a variable steps which will count the number of steps involved in euclid's algorithm.
                      steps = 0
#redefine a and b as i and j.
                      a,b = i,j

#using while loop as above to find the gcd of every pair of numbers in i and j.
                      while b!=0:
                              a,b = b,a%b
                              steps+=1

#if steps is greater than max then max will get the value of steps, in this way maximum number of steps will be calculated simply.
                      if steps>max:
                              max = steps

#and also max_pair will also be calculated with the same if statement.
                              max_pairs = (j,i)

#print the max steps and the pair with the max steps.
print(f"the max number of steps for the given value of k is: {max-1}")
print(f"the pair with maximum number of steps for given k is: {max_pairs}")
            
