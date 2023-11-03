def read(file):
    #here we define a read file ,wew wantto read the output of last file
    with open(file) as file:
        #here we are open a file as file
        for i in file:
            #for every i in file
            n=i.strip()
            #strip or take the value put it here of last file or last question filed named as output.txt
            print (n)
            #print n
file="output.txt"
#here we are taking which i wnat to read
print(read(file))   
#print read file 