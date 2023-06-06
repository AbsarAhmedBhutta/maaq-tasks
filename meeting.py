str = 'my name is absar'

dic = {}

for char in str:
    if char is not None:
        dic[char] = str.count(char)

print(dic)


def flattened(nested_list):
    flat_list = []
    for l in nested_list:
        for item in l:
            flat_list.append(item)

    return flat_list


nested_list = [[1, 2, 3, 4], [2, 1, 3, 2], [1, 2, 3, [1, 2, 4], 1]]
print(flattened(nested_list))
