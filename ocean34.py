n = int(input('Enter a number'))       

# it will take i as an input

 
def factorial(n):       

    # we are defining a function named factorial which will print factorial of n number
    
    if n >= 0 :           

        # if n is positive it will muptiply all numbers upto n to 's' which is equal to 1
        s = 1                   

        # initially value of s is equal to 1
        for i in range(1,n+1):     
            s = s*i             
    

    elif n < 0 :              

        # if n  is negative number it will print invalid option
        print('invalid input')
   
    return s 

# it will return 's' to the factorial function

print('The factorial of ',n,'is',factorial(n))  # this state,ment will print the factorial of the given number

