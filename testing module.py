# def wrap(string, max_width):
#     wrapline = ''
#     for i in range(0, len(string), max_width):
#         wrapline += string[i:i + max_width] + '\n'
#
#     return wrapline
#
#
# if __name__ == '__main__':
#     string, max_width = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4
#     result = wrap(string, max_width)
#     print(result)

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    coordinates = sorted([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])

    for coordinate in coordinates:
        print(coordinate)