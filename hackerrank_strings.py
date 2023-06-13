# You are given a string and your task is to swap cases.
# In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    s1 = ''
    for i in s:
        if i.isupper():
            s1 += i.lower()

        else:
            s1 += i.upper()

    return s1


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# Task
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

def split_and_join(line):
    x = line.split(' ')
    y = '-'.join(x)
    return y


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    return print(f'Hello {first} {last}! You just delved into python.')


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# Task
# Read a given string, change the character at a given index and then print the modified string.
def mutate_string(string, position, character):
    l = list(string)

    l[position] = character

    x = ''.join(l)

    return x


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# In this challenge, the user enters a string and a substring. You have to print the number
# of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        for j in range(len(string) + 1):
            if string[i:j] == sub_string:
                count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

#
# Task
#
# You are given a string .
# Your task is to find out if the string  contains: alphanumeric
# characters, alphabetical characters, digits, lowercase and uppercase
# characters.


if __name__ == '__main__':
    s = input()

has_alnum = False
has_alpha = False
has_digit = False
has_lower = False
has_upper = False

for i in s:
    if i.isalnum():
        has_alnum = True
    if i.isalpha():
        has_alpha = True
    if i.isdigit():
        has_digit = True
    if i.islower():
        has_lower = True
    if i.isupper():
        has_upper = True

print(has_alnum)
print(has_alpha)
print(has_digit)
print(has_lower)
print(has_upper)









