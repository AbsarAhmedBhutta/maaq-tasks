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
    'history': 95,
}
print(grades)
# Merge the grades dictionary into the student dictionary.
student.update(grades)
print(student)

# Print the length of the student dictionary.
print(len(student))
# Sort the keys of the merged_dict dictionary in ascending order and print them.

sorted_s = sorted(student.items(), reverse=True)
print(sorted_s)

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

# Dictionary Comprehension: Write a Python program to create a new dictionary using dictionary comprehension,
# given a list or another dictionary.

new_dict1 = {x: x ** 2 for x in range(12)}
print(new_dict1)

# Nested Dictionaries: Write a Python program to create and manipulate nested dictionaries, where the values of
# certain keys are dictionaries themselves.
nested_dict = {
    'person1': {
        'name': 'John',
        'age': 30,
        'address': {
            'street': '123 Main St',
            'city': 'New York',
            'country': 'USA'
        }
    },
    'person2': {
        'name': 'Alice',
        'age': 25,
        'address': {
            'street': '456 Park Ave',
            'city': 'San Francisco',
            'country': 'USA'
        }
    }
}

person1_name = nested_dict['person1']['name']
print(person1_name)

person2_address = nested_dict['person2']['address']
print(person2_address)

person2_address_modified = nested_dict['person2']['address']['country'] = 'pakistan'
print(person2_address_modified)
print(nested_dict)

# Dictionary Conversion: Write a Python program to convert a dictionary into a list, tuple, or set, and vice versa.
print(list(new_dict1.items()))

# __________________________________________________-



