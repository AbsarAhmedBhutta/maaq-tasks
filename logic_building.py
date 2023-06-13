#  some Python tasks that can help you improve your logical problem-solving skills:

# Factorial Calculation: Create a function that calculates the factorial of a given number.
#
def factorial(n):
    if n == 0:
        print('enter valid ')
    elif n == 1:
        return 1
    else:
        fac = 1
        for i in range(2, n + 1):
            fac *= i

        return fac


print(factorial(5))

# Find the Largest Number: Write a program that takes a list of numbers as input and finds the largest number in the
# list.

list22 = [22, 3, 5, 66, 344, 78, 88, 6, 24]
maxx = list22[0]
for i in range(len(list22)):
    if list22[i] > maxx:
        maxx = list22[i]

print(maxx)

#
# Check for Prime Numbers: Implement a function that checks if a given number is prime or not.

n = 17
is_prime = True

if n < 1:
    is_prime = False

for i in range(2, int(n / 2) + 1):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime")
else:
    print("Not prime")

# Find the Missing Number: Write a program that takes a list of numbers from 1 to N (with one number missing) and
# finds the missing number.

list_missing = [1, 2, 3, 4, 5, 7, 8, 9, 10]
n = 10
total = int(n * (n + 1) / 2)
sum = 0
for i in list_missing:
    sum += i

missing_digit = total - sum
print(missing_digit)

# Palindrome Number: Create a function that checks if a given number is a palindrome (reads the same forwards and
# backwards).

str3 = 'rar'
str4 = 'rar'

if str3 == str4[::-1]:
    print('palindrome')
else:
    print('not palindrome')

# Fibonacci Series: Write a program that generates the Fibonacci series up to a specified number of terms.

n1 = 0
n2 = 1
count = 0
terms = 10

if terms == 0:
    print('error')
elif terms == 1:
    print(n1)
else:
    while count < terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

# Count the Occurrences: Write a program that counts the occurrences of each element in a list and returns the
# results as a dictionary.

list = [2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6]
lists_dict = {}

for i in list:
    if i in lists_dict:
        lists_dict[i] +=1
    else:
        lists_dict[i] = 1

print(lists_dict)

