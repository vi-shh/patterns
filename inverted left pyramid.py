#This code to print Inverted left half pyramid
n=int(input("Enter no of rows:"))
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(" ",end=' ')
    for k in range(0,i):
        print("*",end=' ')
    print("\n")