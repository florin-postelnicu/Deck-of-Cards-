'''
Some methods associated with  class list

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''

import random

# Will start by creating a list

new_list = [ 'a', 'b', 'c', 'd', 'e', 'f']

# shuffle() is a method that randomizes the elements in the list
# the result of this operation is stored in the same container
# new_list

print(new_list)
print()
random.shuffle(new_list)
print(new_list)

# a list can be reordered by using the class list method sort()

print('Using the sort() method')
new_list.sort()
print(new_list)

# a list could be sorted in reversed order with reverse()

print("Reverse the order in the new_list with reverse()")

new_list.reverse()
print(new_list)


# The class list has methods to remove items from a list

new_list.sort()
print(new_list)

# using pop() method to remove the last element in the list
new_list.pop()
print(new_list)

# using append(element) , a new element can be added to the  list
new_list.append('f')
print(new_list)

# the method pop(index) can be used to remove an element in the list
# at a specified position

new_list.pop(0) # this removes the first element of the list
print(new_list)

new_list.append('a')
print(new_list)
new_list.sort()
print(new_list)

# the remove(element) method, removes the first specified element in the list

new_list.remove("c")
print(new_list)

new_list.append('c')
new_list.sort()
print(new_list)

# the insert(position) method adds an element at a certain position

new_list.insert(3,"c")
print(new_list)

# count(value) is a method that returns the number of elements with a specific value

print(new_list.count('c'))
new_list.remove('c')
print(new_list)

# the index(value) returns the index of the first element with the specific value
new_list.insert(3,"c")
print(new_list)
print(new_list.index('c'))

# the copy() method returns a copy of a list

copy_list = new_list.copy()
print(copy_list)

# the clear() method removes all the elements from a list

copy_list.clear()

print(copy_list)
