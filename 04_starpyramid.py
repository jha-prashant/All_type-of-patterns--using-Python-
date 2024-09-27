n=5
for i in range(1,n): 
    print(" ")
    for j in range(1,n-i):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end=" ")
    print()