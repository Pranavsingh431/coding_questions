#define a function named median.
def median(l):
    #define n as the length of the unsorted list l.
    n = len(l)

    # using if len l is 0 then return us none.
    if n == 0:
        return None

    # Define a function to find the median using partition.
    def partition(l, small, big):
        # we have to find middle element and that will be low +high //2 of l 
        mid = l[(small + big) // 2]

        #
        i,j = small,big

        # when i<=j
        while i <= j:
            #l[i<mid]
            while l[i] < mid:
                i += 1

            #this will give us as l of j > mid
            while l[j] > mid:
                j -= 1

            # if left one is less than then interchange the position of the l of i and l of j 
            if i <= j:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1

        return i

    # here we will define a function named qselect(l,small,big,n)
    def qselect(l, small, big, n):
        # if small =big ,then congratulations we have find the median
        if small == big:
            return l[small]

        # 
        midin_index = partition(l, small, big)

        
        leftin_length = midin_index - small+ 1

        # when n<left in length
        if n < leftin_length:
            # median will be in left 
            return qselect(l, small, midin_index - 1, n)
        elif n == leftin_length:
            # congratulation we have find the median
            return l[midin_index]
        else:
            #or it will return lenght mid_index
            return qselect(l, midin_index + 1, big, n - leftin_length)

    # here we will perform floor devision for finding median_index
    median_index = n // 2

    #using quicksort to find the median.
    median_element = qselect(l, 0, n - 1, median_index)

    return median_element

#here we will take a list l 

l = [13,56,50,67,78,98,34,65,87,102]

#print(median(l))
print(median(l))
    
        