lst1=[4,5,6,7,8]
lst2=[9,10,11,12,13]
#to add two lists we can use + operator
lst3=lst1+lst2
print(lst3)
#to repeat a list we can use * operator
lst4=lst1*2
print(lst4) 
#to check if an element is in a list we can use in operator
print(5 in lst1)
print(10 in lst1)
#to check the length of a list we can use len() function
print(len(lst1))
#to find the index of an element in a list we can use index() method
print(lst1.index(6))
#to find the count of an element in a list we can use count() method
print(lst1.count(5))
#to sort a list we can use sort() method
lst1.sort()
#desc sort a list
lst1.sort(reverse=True)
print(lst1)
#insert an element at a specific index we can use insert() method
lst1.insert(2,10)
print(lst1)
#append an element at the end of the list we can use append() method
lst1.append(15)
print(lst1)
#to remove an element from a list we can use remove() method
lst1.remove(10) 
print(lst1)
#to pop an element from a list we can use pop() method
lst1.pop(2)
print(lst1)
#to clear a list we can use clear() method
lst1.clear()
print(lst1)
#using append u can append another list to a list but it will append the whole list as a single element like nested
lst1.append(lst2)
print(lst1)
#to extend a list with another list we can use extend() method
lst1.extend(lst2)
print(lst1)
#to copy a list we can use copy() method
lst5=lst1.copy()
print(lst5)
#to reverse a list we can use reverse() method
lst1.reverse()
print(lst1)
#to find the minimum and maximum element in a list we can use min() and max() functions
print(min(lst1))
print(max(lst1))
#to find the sum of elements in a list we can use sum() function
print(sum(lst1))
#to find the average of elements in a list we can use sum() and len() functions
print(sum(lst1)/len(lst1))
#to remove duplicates from a list we can use set() function
lst6=list(set(lst1))
print(lst6)
#lst[0]=10 #to change the value of an element in a list we can use index and assignment operator
#to return a list ele index use print(lst1.index(ele))
#this returns only the first index of the element if there are multiple occurrences of the element in the list.
#lst1.remove(ele)
#this removes the first occurrence of the element in the list if there are multiple occurrences of the element in the list.
