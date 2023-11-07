def cipher(b,n):#here we are defining a function named function (s,n)
    a=''
    #creating a empty string 
    for i in b:
        #for i in b
        if i.islower():
            a=a+chr((ord(i)+n-97)%26+97)#if i is in lowercase then the individual character moves its value by n i.e alphabets move by a provided distace    
    return a
b=str(input())#user input
n=int(input())
print(cipher(b,n))