# Linear search algorithm
"""
A simple search algorithm to check through the values of a list
"""


def linear_search(list_data, key):
    position = 0
    flag = False

    while position < len(list_data) and not flag:
        if list_data[position] == key:
            flag = True
        else:
            position += 1

    return flag


# data for the algorithm
list_data = [44, 26, 892, 34, 21, 90, 0, 59]
# application of the algorithm,
# where the second argument passed is the `key`
found = linear_search(list_data, 26)
# `found` will result in a boolean value of TRUE or FALSE
print("Element is found,", found)
