#define a function named binary on which various operations will be performed to get the binary ouput of a number.
def binary(x):

#an empty string y is defined to store the output.
         y = ''
         if x == 0:
               return '0'

#if x>0 the remainder will be calculated and it will be converted into a string and will be added to the empty string y and x//2 will be the new value of x.
         while x>0:
               r = x%2
               y = str(r)+y
               x = x//2
     
#after the stopping of the loop the full binary of the given number will be calculated.
         return y

#now we take the input and pass it into the function named binary which we created earlier and the result will be calculated.
n = int(input("enter a number: "))

result = binary(n)
print(result)
