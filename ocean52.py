def merge(L):
    #here we are defining a function  named merge (l)

    if len(L) > 1:
        #if lenght of l list is greater than 1 
        a = len(L)//2
        #here we will divide the list in two parts
        l = L[:a]
        #the right side of list which is creted by a=lenl//2
        r = L[a:]
        #same as first in this case it will be left list
        merge(l)
        #doing same thing as we do on l 
        merge(r) 
        b=0
        c=0
        d=0
        while b < len(l) and c < len(r):#b is smallerr than len of l and c is smaller than len r
            if l[b] < r[c]:
                L[d] = l[b]
                b += 1
            else:
                L[d] = r[c]#if not ,then l[d] = r[c]
                c += 1
            d += 1
            #add 1 in c and d each time
        while b < len(l):#while b is less than length of list then the the values in list are listed according to left part of sorted list
            L[d] = l[b]
            b += 1
            d += 1
        while c < len(r):
            L[d] = r[c]
            c += 1
            d += 1
def printList(L):# here we are defining a function print list
    for i in range(len(L)):
        print(L[i], end=" ")
    print()

L = [69,78,7009,650,65,5004] 
merge(L)
printList(L)