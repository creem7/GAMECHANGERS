# Program to find the largest number in a list.
def maximum_number_in_list(list):
    maximum = list[0]
    for i in list:
        if i > maximum:
            maximum = i
    return maximum
print(maximum_number_in_list([10, 15, 2, 9, 5003, 620, 5040]))