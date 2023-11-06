def max_subarray(list):#here we are defining a function subarray
    max=list[0]#at the firdt the firdt element is maximum so far
    sum=0#and sum is 0
    
    for i in range(len(list)):
        #for i in range len l menas we have to check every elemnt in l
        sum=sum+list[i]#and sum= sum +list[i]
        
        if max<sum:#when max is less than sum
            max=sum
            #max=sum
             
        if sum<0:
            sum=0
            
    print(max)
list=[-2, -1,-5,5,-1,3,1,-1,4]#input list
max_subarray(list)