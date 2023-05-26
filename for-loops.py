def for_else():
    successful = False
    for i in range(5):
        print('Attempt', i)
        if successful:
            print('Attempt successful')
            break
    else:
        print('Attempted four times but failed')


# nestedLoops
def coords():
    for i in range(3):
        for j in range(3):
            print(f"({i},{j})")


def select_sorting(t_nums, lst):
    for i in range(t_nums):
        for j in range(i, t_nums):
            if lst[i] > lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    return lst


# lst = []
# try:
#     t_nums = int(input("Please enter the Total Number of List Elements: "))
#     for i in range(t_nums):
#         value = int(input("Please enter the Value of %d Element : " % i))
#         lst.append(value)
#     sorted_list = select_sorting(t_nums, lst)
#     print("Element After Sorting List in Ascending Order is : ", sorted_list)
# except:
#     print("Error: You must enter a valid number.")


for i in range(0, 10):
    if i % 2 == 0:
        print(i)


