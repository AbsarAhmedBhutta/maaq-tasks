# Task 1: List Operations
# Write a function that takes in a list of integers as input and returns the sum of all the numbers in the list.

def sum_all(l1):
    sum_of_all = 0
    for i in l1:
        sum_of_all += i

    return sum_of_all


l1 = [2, 4, 6, 1]
print(sum_all(l1))


# Task 2: List Manipulation Write a function that takes in a list of strings as input and returns a new list with all
# the strings converted to uppercase.

def string_upper(string_list):
    string_list_upper = []
    for i in string_list:
        x = i.upper()
        string_list_upper.append(x)
    return string_list_upper


string_list = ['absar', 'ali', 'afraz', 'asghar']
print(string_upper(string_list))


# Task 3: List Filtering Write a function that takes in a list of numbers as input and returns a new list containing
# only the even numbers from the original list.

def filer_evens(filer_evens_list):
    even_list = []
    for i in filer_evens_list:
        if i % 2 == 0:
            even_list.append(i)

    return even_list


filer_evens_list = [1, 4, 2, 5, 7, 9, 6, 2, 4]
print(filer_evens(filer_evens_list))


# Task 4: List Sorting Write a function that takes in a list of strings as input and returns a new list with the
# strings sorted in alphabetical order.

def sorting(l3):
    n = len(l3)
    for i in range(n):
        for j in range(i, n):
            if l3[i] > l3[j]:
                temp = l3[i]
                l3[i] = l3[j]
                l3[j] = temp
    return l3


l3 = ['m', 'a', 'l', 'b', 'r', 't']
print(sorting(l3))


# Task 5: List Searching Write a function that takes in a list of strings and a target string as input. The function
# should return True if the target string is present in the list, and False otherwise.

def searching(l4, target):
    for i, stg in enumerate(l4):
        if target == stg:
            return True
        else:
            return False


l4 = ['m', 'a', 'l', 'b', 'r', 't']
target = 'z'
print(searching(l4, target))


# Task 6: List Comprehension Write a function that takes in a list of numbers and returns a new list containing only
# the squares of the numbers in the original list, using list comprehension.

def sqr(i_list):
    # n_s_list = []
    # for i in i_list:
    #     j = i**2
    #     n_s_list.append(j)

    n_s_list = [i ** 2 for i in i_list]
    return n_s_list


i_list = [2, 3, 5, 7, 8]
print(sqr(i_list))


# Task 7: List Concatenation Write a function that takes in two lists as input and returns a new list that is the
# concatenation of the two input lists.

def concatenation(list_one, list_two):
    l = list_one + list_two
    return l


list_one = [2, 3, 4]
list_two = [4, 5, 8]

print(concatenation(list_one, list_two))


# Task 8: List Slicing Write a function that takes in a list of numbers and returns a new list containing the first
# three numbers from the original list.
def slice(ist_one):
    l = ist_one[:3]
    return l


ist_one = [2, 3, 4, 10, 2, 1, 7, 9]
print(slice(ist_one))

# Task 9: List Reversal
# Write a function that takes in a list of strings and returns a new list with the strings in reverse order.
print(l4[::-1])


# Task 10: List Counting Write a function that takes in a list of integers and a target integer as input. The
# function should return the number of times the target integer appears in the list.

def task_10(li5, target):
    count = 0
    for i, item in enumerate(li5):
        if target == item:
            count += item
    return count


li5 = [1, 2, 1, 2, 1, 3, 4, 4, 5, 6, 7, 10]
target = 1
print(task_10(li5, target))


# Task 1: List Flattening Write a function that takes in a nested list of integers and returns a new list that is a
# flattened version of the input list. The flattened list should contain all the integers from the nested list in a
# single level.

def flattened(nested_list):
    flat_list = []
    for l in nested_list:
        for i in l:
            flat_list.append(i)
    return flat_list


nested_list = [[4, 3, 2, 2, 4], [4, 5, 67, 88, 99, 00], [222, 33, 444, 555, 666, 777]]

print(flattened(nested_list))


# Task 2: List Partitioning Write a function that takes in a list of integers and a target integer as input. The
# function should return a new list that partitions the input list into two sublists: one containing all the numbers
# less than the target, and the other containing all the numbers greater than or equal to the target.

def partition(li6, target):
    list_g = []
    list_l = []
    for i in li6:
        if i >= target:
            list_g.append(i)
        else:
            list_l.append(i)
    return list_l, list_g


li6 = [77, 666, 43, 2, 6, 77, 9, 0, 9, 8, 1]
target = 1

result = partition(li6, target)
list_l, list_g = result

print(list_g)
print(list_l)

# Task 4: List Palindrome Write a function that takes in a list of strings and returns True if the list is a
# palindrome (reads the same forwards and backwards), and False otherwise.
l7 = ['rare']
if l7[0] == l7[0][::-1]:
    print('true')
else:
    print('false')


# Task 5: List Intersection Write a function that takes in two lists of integers and returns a new list that contains
# only the elements that are common to both input lists.
def list_intersection(list1, list2):
    intersection = []
    for num in list1:
        if num in list2 and num not in intersection:
            intersection.append(num)
    return intersection


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(list_intersection(list1, list2))


# Task 8: List Merging Write a function that takes in two sorted lists of integers and returns a new list that merges
# the two input lists into a single sorted list.


def merge(l1_sorted, l2_sorted):
    new = sorted(l1_sorted + l2_sorted)
    return new


l1_sorted = [42, 43, 44, 56, 66]
l2_sorted = [1, 2, 3, 4, 5]
print(merge(l1_sorted, l2_sorted))





