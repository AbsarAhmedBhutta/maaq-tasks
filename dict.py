# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

dict1 = {}

for x in range(1, 11):
    dict1[x] = x ** 2

print(dict1)

# Create a dictionary called student with the following key-value pairs: "name" with a value of "John", "age" with a
# value of 20, and "major" with a value of "Computer Science".
student = {
    'name': 'john',
    'age': 20,
    'major': 'Computer Science'
}
# Add a new key-value pair to the student dictionary for "university" with a value of "ABC University".
student['university'] = 'ABC University'

print(student)
# Access and print the value of the "age" key in the student dictionary.
print(student['age'])
# Update the value of the "major" key in the student dictionary to "Data Science".
student['major'] = 'Bio'
print(student)
# Check if the key "address" exists in the student dictionary. Print "Yes" if it exists and "No" otherwise.
if 'address' in student:
    print('yes')
else:
    print('no')
# Remove the key-value pair for "major" from the student dictionary.
del student['major']
print(student)
# Use a for loop to iterate over the key-value pairs in the student dictionary and print each key-value pair on a new
# line.
for key, vals in student.items():
    print(key, ':', vals)
# Create a dictionary called grades with the following key-value pairs: "math" with a value of 90, "english" with a
# value of 85, and "history" with a value of 95.
grades = {
    'math': 90,
    'english': 85,
    'history': 95
}

# Merge the grades dictionary into the student dictionary.
student.update(grades)
print(student)

# Print the length of the student dictionary.
print(len(student))
# Sort the keys of the merged_dict dictionary in ascending order and print them.

sorted_s = sorted(student.keys())
for key in sorted_s:
    print(key)

# Here are some advanced-level dictionary practice tasks:
#
# Word Frequency Counter: Write a function that takes a string as input and returns a dictionary containing the
# frequency of each word in the string. For example,
# if the input is "I love to code, and coding is fun!", the output should be {'i': 1, 'love': 1, 'to': 1, 'code': 1,
# 'and': 1, 'coding': 1, 'is': 1, 'fun': 1}.

string = 'I love to code code and coding is fun!'

words = string.split()
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)

# Write a function named flatten_dictionary that takes a nested dictionary as input and returns a flattened
# dictionary. The flattened dictionary should only contain keys that represent the full key path to the leaf nodes of
# the original nested dictionary. The values in the flattened dictionary should be the corresponding values of the
# leaf nodes.

dict = {
    'a': {'b': {'c': 1, 'd': 2}, 'e': 3}, 'f': 4
}


# Dictionary Merge: Write a function that takes multiple dictionaries as input and merges them into a single
# dictionary. If there are any common keys, combine their values into a list. For example, if the input is {'a': 1,
# 'b': 2}, {'b': 3, 'c': 4}, and {'c': 5, 'd': 6}, the output should be {'a': 1, 'b': [2, 3], 'c': [4, 5], 'd': 6}.
#
# Anagram Grouping: Given a list of words, group the anagrams together and return the groups as a dictionary.
# Anagrams are words that have the same letters but in a different order. For example, if the input is ['eat', 'tea',
# 'tan', 'ate', 'nat', 'bat'], the output should be {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'],
# 'abt': ['bat']}.
#
# Dictionary Inversion: Write a function that takes a dictionary as input and returns a new dictionary where the keys
# and values are inverted. If multiple keys have the same value, combine them into a list. For example, if the input
# is {'a': 1, 'b': 2, 'c': 2}, the output should be {1: 'a', 2: ['b', 'c']}.
