#enter a number
x = int(input("Enter a number: "))

#generalising 7 and 5 as a and b.
a = 7
b = 5

#if x divides 7 and the remainder is zero it is divisible by 7 and same applies for 5 also.

if (x%a == 0 and x%b == 0):
    print("the number is divisible by both 7 and 5.")

else:
    print("the number is not divisible by 7 and 5.") 
