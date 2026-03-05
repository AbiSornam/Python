String='Hello'
print(String[0:5]) # it will print from index 0 to 4 (5-1)
print(String[0:5:2]) # it will print from index 0 to 4 with a step of 2 (5-1)
print(String[::2]) # it will print the whole string with a step of 2
print(String[1:5:2]) # it will print from index 1 to 4 with a step of 2 (5-1)
print(String[-5:-1]) # it will print from index -5 to -2 (-1-1)
print(String[-5:-1:2]) # it will print from index -5 to -2 with a step of 2 (-1-1)
list=[1,2,3,4,5]
print(list[0:5]) # it will print from index 0 to 4
print(list[0:5:2]) # it will print from index 0 to 4 with a step of 2
print(list[::2]) # it will print the whole list with a step of 2
tuple=(1,2,3,4,5)
print(tuple[0:5]) # it will print from index 0 to 4
print(tuple[0:5:2]) # it will print from index 0 to 4 with a step of 2
print(tuple[::2]) # it will print the whole tuple with a step of 2
#in tuples , if not present it will return empty tuple but others causes error!
