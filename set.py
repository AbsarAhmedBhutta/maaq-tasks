# Set Intersection: Write a Python program to find the intersection of two sets.
s3 = {1, 2, 3, 5, 6}
s4 = {6, 7, 8, 1}

i_set = s3.intersection(s4)
print(i_set)

# Set Difference: Write a Python program to find the difference between two sets.
s3 = {1, 2, 3, 5, 6}
s4 = {6, 7, 8, 1}

d_set = s4 - s3
print(d_set)
# Set Union: Write a Python program to find the union of two sets.

s1 = {1, 2, 3, 5, 6}
s2 = {6, 7, 8, 1}

u_set = s1.union(s2)
print(u_set)
# Set Symmetric Difference: Write a Python program to find the symmetric difference between two sets.
s1 = {1, 2, 3, 5, 6}
s2 = {6, 7, 8, 1}

sy_set = s1.symmetric_difference(s2)
print(sy_set)
# Subset Check: Write a Python program to check if one set is a subset of another set.

s5 = {1, 2, 3, 5, 6}
s6 = {1, 2, 3}

is_sub = s6.issubset(s5)
print(is_sub)
# Set Comprehension: Write a Python program to create a new set using set comprehension, given a list or another set.
new_set = {i for i in range(5)}
print(new_set)
# Set Operations: Write a Python program to perform various set operations like adding elements, removing elements,
# and checking membership.
new_set.add('b')
print(new_set)
new_set.remove(1)
print(new_set)
new_set.pop()
print(new_set)
for i in new_set:
    if i == 'b':
        print('True')

# Set Conversion: Write a Python program to convert a list or tuple into a set.
l = [1, 2, 3]
t = tuple(l)
print(t)



setss = {1, 2, 3, 4}
setss.add('a')
print(setss)
