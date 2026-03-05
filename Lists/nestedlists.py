lst=[[1,2,3],[4,5,6],[7,8,9]]
print(lst[0]) #to access the first list
print(lst[0][1]) #to access the second element of the first list
#to iterate through a nested list we can use nested loops
for i in lst:
    for j in i:
        print(j,end=' ')
    print() #to print new line after each inner list is printed