#taking input to enter any year.
x = int(input("Enter any year: "))
#as leap year occur once in every 4 years so if a number divides 4 and also if it is not divisible by 100 then it is a leap year.
if ((x%400 == 0)or(x%4 == 0 and x%100 !=0)):
   print("It is a leap year")

#else it is not a leap year.
else:
   print("It is not a leap year")
