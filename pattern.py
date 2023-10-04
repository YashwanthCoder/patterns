#patterns
n=int(input("how many patterns="))
for i in range(n+1):
    for n in range(i+1):
        print("*",end=" ")
    print()
