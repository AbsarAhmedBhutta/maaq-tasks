# ---------------Lists:
#
# Implement a function to reverse a list in-place without using any built-in methods.

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

    new_list = left_list + [pivot] + right_list

    return new_list


list2 = [1, 2, 3, 34, 5, 6, 22, 22]
print(list2)
print(partition_list(list2))

def kth_smallest(list_2, k):
    left_list = []
    right_list = []
    pivot = 6

    for item in list_2:
        if item > pivot:
            right_list.append(item)
        else:
            left_list.append(item)

    left_list1 = sorted(left_list)
    right_list2 = sorted(right_list)

    if k == pivot:
        return k
    elif k > pivot:
        for i in right_list2:
            return right_list2[i]
    else:
        for j in left_list1:
            return left_list1[j]


list3 = [1, 2, 3, 34, 5, 6, 22, 22]
k = 4
print(kth_smallest(list3, k))


# Create a list comprehension that filters out duplicates from a given list while preserving the original order.

list4 = [1, 2, 3, 34, 5, 6, 22, 22, 2, 2]

new_l1 = [list(set(list4))]
print(new_l1)

# Write a function that finds the longest increasing subsequence in a list and returns its length.


# -------------Tuples:
#
# Create a tuple of coordinates representing points in a 2D space, and implement a function to find
# the closest pair
# of points.


# Write a program that takes multiple tuples as input and sorts them based on a specific element within
# each tuple.
# Create a function that accepts a tuple of integers and returns a new tuple with the elements reversed.

# Implement a function that finds the maximum sum of non-adjacent elements in a tuple of integers.
#
# Write a program
# that computes the dot product of two tuples representing vectors.
#
# --------------------Sets:
#
# Create a program that finds the union, intersection, and difference of two sets.

# Implement a function that checks whether a set is a subset of another set.

# Write a program to find the symmetric difference between two sets.

# Create a function that calculates the Jaccard similarity coefficient between two sets.

# Implement a set-based solution to solve the classic "N-Queens" problem.

# ------------------- Dictionaries:
#
# Write a function that merges two dictionaries, combining the values of common keys.

# Implement a program that finds the key with the highest value in a dictionary.

# Create a function that counts the frequency of each word in a given sentence using a dictionary.

# Write a program that checks if two dictionaries have the same keys but potentially different values.

# Implement a dictionary-based cache that stores the results of expensive function calls and retrieves
# them when needed.
