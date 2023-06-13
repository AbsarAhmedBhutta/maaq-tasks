# Implement a function to reverse a list in-place without using any built-in methods.
import math

list1 = [1, 2, 3, 34, 5, 6, 22, 22]
print(list1[::-1])


def reverse_list(my_list):
    reversed_list = []
    len_l = len(my_list)
    for i in range(len_l - 1, -1, -1):
        reversed_list.append(my_list[i])
    return reversed_list


my_list = [1, 2, 3, 34, 5, 6, 22, 22]
print(reverse_list(my_list))


# Write a function to find the kth smallest element in a list using a quickselect algorithm.

def partition_list(list_2):
    left_list = []
    right_list = []
    pivot = 6

    for item in list_2:
        if item > pivot:
            right_list.append(item)
        else:
            left_list.append(item)

    new_list = left_list + right_list

    return new_list


list2 = [1, 2, 3, 34, 5, 6, 22, 22]
print(list2)
print(partition_list(list2))


def kth_smallest(list_2, k):
    left_list = []
    right_list = []
    pivot = list_2[5]

    for item in list_2:
        if item > pivot:
            right_list.append(item)
        else:
            left_list.append(item)

    left_list1 = sorted(left_list)
    print(left_list1)
    right_list2 = sorted(right_list)
    print(right_list2)

    if k == pivot:
        return k
    elif k > pivot:
        return right_list2[k - pivot - 1]
    else:
        return left_list1[k - 1]


list3 = [1, 2, 3, 34, 5, 6, 22, 22]
k = 2
print('kth_smallest:- ', kth_smallest(list3, k))

# Create a list comprehension that filters out duplicates from a given list while preserving the original order.

list4 = [1, 2, 3, 34, 5, 6, 22, 22, 2, 2]

new_l1 = [list(set(list4))]
print(new_l1)

# 2 sum problem

l3 = [2, 3, 4, 9, 3, 6, 10]
t = 11
for i in range(len(l3)):
    for j in range(len(l3)):
        if l3[i] + l3[j] == t:
            print(l3[i], l3[j])

# Write a program that takes multiple tuples as input and sorts them based on a specific element within
# each tuple.

tuples_l = [('Jack', 76), ('Beneth', 78), ('Cirus', 77), ('Faiz', 79)]
tuples_l.sort(key=lambda a: a[0])
print(tuples_l)

# Create a function that accepts a tuple of integers and returns a new tuple with the elements reversed.

tuples = (1, 2, 2, 3, 4, 5, 3)
print(tuples[::-1])

# Write a program
# that computes the dot product of two tuples representing vectors.

vec2 = (1, 3, 4, 5, 6, 7)
vec1 = (2, 22, 33, 4, 55, 66)

if len(vec2) != len(vec1):
    print('error')
else:
    dot_product = 0
    for i in range(len(vec1)):
        dot_product += vec2[i] * vec1[i]

    print(dot_product)

# Create a program that finds the union, intersection, and difference of two sets.

# union
setA = {1, 2, 3, 4, 5}
setB = {6, 7, 8, 9, 5}

res = []

for i in setA:
    res.append(i)
for j in setB:
    res.append(j)

print(set(res))
print(setA.union(setB))
# intersection

res_inter = []

for i in setA:
    for j in setB:
        if i == j:
            res_inter.append(i)

print(setA.intersection(setB))

print(res_inter)

# difference

res_diff = []
setC = []

for i in setA:
    setC.append(i)
for j in setB:
    if j not in setC:
        res_diff.append(j)

print(res_diff)

# Implement a function that checks whether a set is a subset of another set.

s1 = {1, 2, 3}
s2 = {0, 9, 1, 3, 6, 7}
l = []
for i in s2:
    for j in s1:
        if j == i:
            l.append(j)

l1 = set(l)

if s1 == l1:
    print('TRUE')
else:
    print('FALSE')

# Write a function that merges two dictionaries, combining the values of common keys.

dict1 = {1: 'a', 2: 'b', 3: 'c'}
dict2 = {5: 'a', 2: 'b', 4: 'c'}

for k, v in dict2.items():
    if k in dict1:
        dict1[k] = dict1[k] + ',' + v

print(dict1)

# ___________substring__________

str3 = 'absar'

for i in range(len(str3)):
    for j in range(len(str3)):
        print(str3[i:j])

# _______________
