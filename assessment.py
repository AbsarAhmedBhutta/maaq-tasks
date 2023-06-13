s = '''("Player's Lounge", 'c320002', 'Black Coffee', 2, 'Kitchen', '98', 1, 4)'''

s = s[1:-1]
s = s.replace("'", "")
print(s)
s = s.replace('"', "")
print(s)
list1 = s.split(",")
print(list1)

txt = ",,,,,rrttgg.....bana'na....rrr"
x = txt.strip(",.grt")
x2 = x.replace("'", "")
print(x2)


# Problem Statement –
#
# There are some groups of devils and they splitted into people to kill them. Devils make People to them left as
# their group and at last the group with maximum length will be killed. Two types of devils are there namely “@” and
# “$” People is represented as a string “P”
#
# Input Format:
# First line with the string for input
#
# Output Format:
# Number of groups that can be formed.
#
# Constraints:
# 2<=Length of string<=10^9
#
# Input string
# PPPPPP@PPP@PP$PP
#
# Output
# 7
#
# Explanation
# 4 groups can be formed
#
# PPPPPP@
# PPP@
# PP$
# PP
# Most people in the group lie in group 1 with 7 members.


# s = 'PPPPPP@PPP@PP$PP'
# count = 0
# for i in range(len(s)):
#     for j in range(len(s)):
#         print(s[i:j])
#

def count_groups(string):
    groups = string.split('@')
    num_groups = 0
    for group in groups:
        subgroups = group.split('$')
        print(subgroups)
        num_groups += len(subgroups)
    return num_groups


string = "PPPPPP@PPP@PP$PP"
print(string.split('@'))
result = count_groups(string)
print(result)
