#enter marks of 5 subjects.
a = int(input("enter the marks in subject 1: "))
b = int(input("enter the marks in subject 2: "))
c = int(input("enter the marks in subject 3: "))
d = int(input("enter the marks in subject 4: "))
e = int(input("enter the marks in subject 5: "))


#calculate the average marks with the help of the five subjects.
avg = (a+b+c+d+e)/5

#now by using the given conditions us if else statements to calculate the grade.
if avg>=90:
   print("grade is A")
elif 80<=avg<90:
   print("grade is B")
elif 70<=avg<80:
   print("grade is C")
elif 60<=avg<70:
   print("grade is D")
else:
   print("grade is F")
