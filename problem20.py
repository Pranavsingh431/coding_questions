#define a function named parabola which takes curvature and number of stars as input.
def parabola(a, num_stars):
    for y in range(-num_stars//2 , num_stars // 2+1):

#using the basic equation of parabola to get the corresponding values of x and printing the desirable spaces and * between it.
        x = int(a * y ** 2)
        print((" " * (num_stars//2 + x) ) + "*" )

#take input of a and num_stars.
a = float(input("Enter the curvature (coefficient 'a' in y = ax^2): "))
num_stars = int(input("Enter the number of stars: "))

#print the function.
parabola(a, num_stars)



