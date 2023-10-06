#enter your age
x = int(input("Enter your age: "))

#if age is less than 18 it will print you are a minor.
if x<18 :
   print("You are a minor")

#if the age is between 18 and 65 it will print you are an adult.
elif (18<=x<=65):
   print("You are an adult")

#else it will print you are a senior citizen.
else:
   print("You are a senior citizen")

