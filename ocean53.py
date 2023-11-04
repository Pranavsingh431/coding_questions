def quicksort(L,l,r):#here we have to so sorting by quick sort mmethod so define a quick sort function
    if l<r:#when l<r
        ps=partition(L,l,r)
        quicksort(L,l,ps-1)#
        quicksort(L,ps+1,r)
        #here what we have done that we are dividing the list in two two parts

def partition(L,l,r):
    #do partition of L,l,r
    i=l 
    j=r 
    p=L[r]
    #id i=l,j=r,p=l[r],then
    while i<j:#while i is less than the rightmost value
        while i<r and L[i]<p:
            i+=1
            #and i <r 
        while j>l and L[j]>p:#if j is greater than leftmost value and jth term in list is greaterthan jth value than decreases by until it is less than left value 
            j-=1
        if i<j:# the values of i and j in the list are swaped
            L[i],L[j]=L[j],L[i]
    if L[i]>p:#if the ith term is greater than p i.e rightmost value then the values are swaped and i is returned 
        L[i],L[r]=L[r],L[i]
    return i
#the i then is used for another partion and by reccursion the list is sorted
L=[300,56,76,900,87,986,537,867]
quicksort(L,0,len(L)-1)
print(L)