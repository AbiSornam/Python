n=5
m=1
for i in range(n):
    for j in range(i+1):
        print(m,end=' ')
        m+=1
        #after end of j loop print new line !
    print()

