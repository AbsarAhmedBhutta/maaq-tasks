# Swap Values: Write a function that takes two integers as input and returns a tuple with the values swapped. For
# example, if the input is (3, 7), the output should be (7, 3).

x, y = 3, 7
t = (x, y)
print(t[::-1])

# Merge Lists: Write a function that takes two lists as input and returns a tuple with the combined elements from
# both lists. For example, if the input is ([1, 2, 3], ['a', 'b', 'c']), the output should be ((1, 'a'), (2, 'b'),
# (3, 'c')).
#

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']

merged = []
for i in range(len(l1)):
    merged.append((l1[i],(l2[i])))

print(tuple(merged))


# Average and Range: Write a function that takes a list of numbers as input and returns a tuple containing the
# average and range of the numbers. The average should be a floating-point number, and the range should be the
# difference between the maximum and minimum values in the list. For example, if the input is [4, 9, 2, 1, 5],
# the output should be (4.2, 8).

l3 = [4, 9, 2, 1, 5]
total = 0
for i in l3:
    total+=i

avg = total/len(l3)
ran = max(l3)-min(l3)
print((avg, ran))


# Extract Information: Write a function that takes a string as input, which represents a person's full name,
# and returns a tuple containing the first name and last name. Assume that the input string contains exactly two
# names separated by a space. For example, if the input is "John Doe", the output should be ('John', 'Doe').

name = "John Doe"
names = name.split()
f_name = names[0]
l_name = names[1]

print((f_name,l_name))


# Count Characters: Write a function that takes a string as input and returns a tuple containing the count of
# uppercase and lowercase letters in the string. For example, if the input is "Hello, World!", the output should be (
# 2, 8), indicating that there are 2 uppercase letters and 8 lowercase letter1s in the string.

input_str = "Hello, World!"
u_case_count = 0
l_case_count = 0

for item in input_str:
    if item.isupper():
        u_case_count += 1
    elif item.islower():
        l_case_count += 1

print((u_case_count, l_case_count))

