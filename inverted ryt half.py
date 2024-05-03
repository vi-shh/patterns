#inverted right half pyramid code 1
n=int(input("Enter the no of rows:"))
for i in range(n):
    for j in range(n,i,-1):
        print("*",end=' ')
    print(" ","\n")
    
