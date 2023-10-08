import random
#creating an empty list.
l = []

# iterating i from 1 to 1000 and repeating random.randiint also 1000 times to add 1000 random numbers in the empty list l.
for i in range(1,1000):
     l.append(random.randint(1,1000))

print(l)
