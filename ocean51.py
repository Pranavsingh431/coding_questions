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
       
                
    
l=[1,3,6,8,5,55,23,88,68]
print(bubblesort(l))
#here we will get the valuue the bubble sort value