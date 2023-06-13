# Here are some Python tasks that can help you improve your problem-solving skills:


# Fibonacci Sequence: Write a program that generates the Fibonacci sequence up to a specified number of terms.

def fibonacci(terms):
    n1 = 0
    n2 = 1
    count = 0
    if terms == 0:
        print("not valid terms")
    elif terms == 1:
        print(n1)
    else:
        while count < terms:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1


terms = 5
fibonacci(terms)

# Palindrome Checker: Create a function that takes a string as input and checks if it is a palindrome
# (reads the same
# forwards and backwards).
import re


def palindrome(str1):
    if str1 == str1[::-1]:
        return True
    else:
        return False


str1 = 'rar'
print(palindrome(str1))


#
# Prime Number Generator: Write a program that generates prime numbers up to a specified limit.

def prime_number_generator(limit):
    prime_nums = []

    for nums in range(2, limit):
        is_prime = True
        for i in range(2, int(nums / 2) + 1):
            if nums % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_nums.append(nums)

    return prime_nums


print(prime_number_generator(30))


# Anagram Checker: Implement a function that takes two strings as input and
# checks if they are anagrams (contain the same characters in a different order).

def anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    char_count = {}
    for i in str1:
        if i in char_count:
            char_count += 1
        else:
            char_count[i] = 1

    for char in str2:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]
        else:
            return False

    if len(char_count) == 0:
        return 'is anagrams'
    else:
        return False


str1 = "listen"
str2 = "silent"

print(anagrams(str2, str1))


# Word Count: Write a function that takes a sentence as input and counts the
# frequency of each word, returning the results as a dictionary.

def word_freq(sentence):
    str = sentence.split(' ')
    char_freq = {}

    for i in str:
        if i in char_freq:
            char_freq[i] += 1
        else:
            char_freq[i] = 1

    return char_freq


sentence = 'how how how are you hope you are fine'
print(word_freq(sentence))


# Password Strength Checker: Create a program that checks the strength of a password based
# on specific criteria, such as length, presence of uppercase/lowercase letters, and special characters.

def strength_check(password):
    if len(password) < 10:
        return 'not strong'

    upper_count = 0
    lower_count = 0
    special_char_count = 0

    for i in password:
        if i.isupper():
            upper_count += 1
        if i.lower():
            lower_count += 1
        if re.match(r'\W', i):
            special_char_count += 1

    if upper_count >= 2 and lower_count >= 2 and special_char_count >= 1:
        return 'strong'
    else:
        return 'not strong'


print(strength_check(password='Aibif#$ubgogeEiAibif#$ubgogeEi'))


# Sum of Digits: Implement a function that calculates the sum of the digits of a given number.

def sum_of_digits(number):
    sum = 0
    for i in number:
        sum += int(i)

    return sum


number = 5555
print(sum_of_digits(str(number)))




