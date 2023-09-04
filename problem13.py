#taking two inputs as strings.
x = input("enter a string: ")
y = input("enter another string: ")


#create any empty string intersperse.
intersperse = ''


#interate two variable i1 and i2 in the zip function of x and y.
for i1,i2 in zip(x,y):

#add i1 and i2 from the loop in the empty string interperse.
    intersperse = intersperse+i1+i2

print(intersperse)

