#take input of a string.
x = input("enter a string: ")

#define 2 variables count1 and count2 as 0.
count1 = 0
count2 = 0
i = 0
l = ['a','e','i','o','u','A','E','I','O','U']
for i in range(len(x)): #we used range to be len(x) because we do not want to get any kind of error in over repeating of the loop.
     if x[i] in l: #if there is any alphabet in x which is in l it will add 1 to the count1 which we defined to be 0.
          count1+=1
     else:
          count2+=1
print("the number of vowels are ",count1)
print("the number of consonants are ",count2)
