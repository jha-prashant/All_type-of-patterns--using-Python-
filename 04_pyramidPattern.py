n=4
for i in range(0,n):
    print(" "*(n-i),end=" ")
    for j in range(0,i+1): 
        print(i,end=" ")
    print()