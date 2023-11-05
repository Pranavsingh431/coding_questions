def bubblesort(l):
    #here we are deffining a function bubble sort l 
    
    for i in range (len(l)):
        #for i in range lenght of l
        for j in range (0,len(l)-i-1):
            #because at the len l value of i , it will be out of inde so we are taking this command
            if l[j]>l[j+1]:
                
        
            
                a=l[j]
                l[j]=l[j+1]
                l[j+1]=a
                #if l[i+1] is bigger then we will exchange position of l[i] and l[i+1]
    return l
       
                
#if not swapped then break

#define a function named merge.
def merge(l):
    
    if len(l) > 1:
        #dividing the list into three parts mid , left, right.
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]

        # using recursion in each half left and right.
        merge(left)
        merge(right)

    
        i = 0
        j = 0
        
        
        x = 0
        
        #using while loop to use the below condition for i and j.
        while i < len(left) and j < len(right):
            #again using if else statement to sort the given chunk of list.
            if left[i] <= right[j]:
                
              # here l of x is equal to left i
              l[x] = left[i]
              #increase the i by 1.
              i += 1
            else:
                l[x] = right[j]
                j += 1
            # Move to the next slot
            x += 1

        
        while i < len(left):
            l[x] = left[i]
            i += 1
            x += 1

        while j < len(right):
            l[x]=right[j]
            j += 1
            x += 1


#define a function named quick_sort.
def quicksort(l):

    if len(l) <= 1:
        return l

    half = l[len(l) // 2]
    #it will half 
    left = [x for x in l if x < half]
    middle = [x for x in l if x == half]
    right = [x for x in l if x > half]

    return quicksort(left) + middle + quicksort(right)


list = ["fruits", "they", "gym", "placement", "system", "iit", "ropar", "gwalior", "computer", "sumit"]
#here we used some string 

# Write the words to the input.txt file using with and open operations.
with open("input.txt", "w") as file:
    #using for loop.
    for word in list:
        file.write(word + "\n")



def file(f):
    #here we are defing a file named f
    with open(f, 'r') as file:
        list = [line.strip() for line in file]
    return list
#it will create a new list in which we have stripped line

#define a function write_file which will display the words line by line.
def wri_file(f, list):
    with open(f, 'w') as file:
        for word in list:
            file.write(word + '\n')

#here we are creating a file varible used variable input f = input.txt

inputf = "input.txt"
output_bubble = "output_bubble.txt"
output_merge = "output_merge.txt"
output_quick = "output_quick.txt"

words = file(inputf)

    #nowwbubble words.copy
wbubble = list.copy()
bubblesort(wbubble)
#add a variable 
wri_file(output_bubble, wbubble)

    #now print the Merge Sort.
wmerge = words.copy()
merge(wmerge)
    #add the input in the text file dedicated to merge sort.
wri_file(output_merge, wmerge)

    #here wquick =words.copy()
wquick = words.copy()
wquick = quicksort(wquick)
    #here we will use write file that will 
wri_file(output_quick, wquick)