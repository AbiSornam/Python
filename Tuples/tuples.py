tup1=("apple","banana","cherry")
tup1+=("orange",) #to add a single element to a tuple we need to add a comma after the element
print(tup1)
#to access elements in a tuple we can use index and slicing just like lists
print(tup1[0]) #to access the first element
print(tup1[1:3]) #to access a range of elements this is slicing
print(tup1[-1]) #to access the last element
#to check if an element is in a tuple we can use in operator
print("banana" in tup1)
print("grape" in tup1)
#to find the length of a tuple we can use len() function
print(len(tup1))
#to find the index of an element in a tuple we can use index() method
print(tup1.index("cherry"))
#to find the count of an element in a tuple we can use count() method
print(tup1.count("banana"))
print(tup1.count("grape"))
#but you cannot append,change,insert an element!
#tuples are immutable but they can contain mutable elements like lists
tup2=(1,2,3,[4,5])
print(tup2)
tup2[3][0]=10 #to change the value of an element in a list inside a tuple we can use index and assignment operator
print(tup2)
#to change tuple to list
tup3=list(tup1)
print(tup3)
#to change list to tuple
list4=tuple(tup3)
print(list4)