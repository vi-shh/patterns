#This code to print left half pyramid
n=int(input("Enter no of rows:"))
for i in range(0,n):
    #print(i)
    for j in range(0,n-i-1):
        #print(j)
        print(" ",end=' ')
    for k in range(0,i+1):
        #print(i)
        print("*",end=' ')
    print("\n")kd
           

