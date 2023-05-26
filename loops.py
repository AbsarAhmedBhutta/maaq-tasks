def print_1_to_10():
    for i in range(0, 11):
        print(i)


def cal_sum_all():
    sum = 0
    for i in range(0, 100):
        sum += i

    print("sum of all :", sum)


def print_all_even():
    for i in range(0, 21):
        if i % 2 == 0:
            print(i)


# Fibonacci Series:


def Fibonacci_Series():
    count = 0
    n_total = 13
    n_1 = 0
    n_2 = 1
    if n_total <= 0:
        print('enter valid number')
    elif n_total == 1:
        print(n_1)
    else:
        while count <= n_total:
            print(n_1)
            nth = n_1 + n_2
            n_1 = n_2
            n_2 = nth
            count += 1


def Prime_Numbers():
    l1 = [int(x) for x in input("enter  numbers").split()]
    sum = 0
    for num in l1:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    print(num, "not prime")
                    break
            else:
                print(num, "prime number")
                sum = sum + num
        else:
            print(num, "not prime")
    print(sum, "sum of prime numbers")


def Factorial_Calculation():
    pass


l1 = ['213', '12763', '213']
for i in range(len(l1)):
    l1[i] = int(l1[i])
    print(type(l1[i]))


l2 = [int(x) for x in l1]
dt = type(l2[0])
print(dt)

