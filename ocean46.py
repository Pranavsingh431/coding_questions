def matrix(a,b):
    #here we are defining a function named matrix to find sum of matrix
    for  i in range (3):
        #here we are taking a 3*3 matrix so i in rnage 3
        for j in range (3):
            #in that matrix we are taking the elements
            c[i][j]=a[i][j]+b[i][j]
            #here we are doing sum of two marix
    return c 
a=[[1,2,3],[5,6,7],[3,4,5]]
b=[[2,4,6],[3,5,7],[1,8,0]]
c=[[0,0,0],[0,0,0],[0,0,0]]
#we are taking the input
print(matrix(a,b))
#this will give us the sum of matrix
    
        