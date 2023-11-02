file =open("output.txt","w")
#here we are first opening a file by open and naming it as output.txt and command w for writing
n=int(input("enter a number"))
#user input
for i in range (1,n+1):
    #here we are giving values from 1 to n
    p=str(i)+'\n'
    #file only take string value,so we are converting i to str and \n for new line
    file.write(p)
    #for writing p in file
file.close()    
#for closing the file