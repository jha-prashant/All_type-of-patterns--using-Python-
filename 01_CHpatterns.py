n = 4
for i in range(0, n-1):
    ch='A'
    for j in range(0,n-1):
        print(ch, end = " ")
        ch = chr(ord(ch)+1)
    print()