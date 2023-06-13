str = 'my name is absar'

dic = {}

for char in str:
    if char is not None:
        dic[char] = str.count(char)

print(dic)


def flattened(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flattened(item))
        else:
            flat_list.append(item)

    return flat_list


nested_list = [[1, 2, 3, 4], [2, 1, 3, 2], [1, 2, 3, [1, 2, 4], [1, 2, 4], 1]]
print(flattened(nested_list))


def conversion(s):
    print(s)

    s = s.replace("(", "")
    s = s.replace(")", "")
    s = s.replace("'", "")
    s = s.replace('"', "")
    list1 = s.split(",")

    print(list1)


s = '''("Player's Lounge", 'c320002', 'Black Coffee', 2, 'Kitchen', '98', 1, 4)'''

conversion(s)


thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-i-1)+c+(c*i).ljust(thickness-i-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).rjust(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).center(thickness*6))