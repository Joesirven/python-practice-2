# Complete the find_second_largest function which accepts
# a list of numerical values and returns the second largest
# in the list
#
# If the list of values is empty, the function should
# return None
#
# If the list of values has only one value, the function
# should return None
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def find_second_largest(values):
#order values
    sorted_list = sorted(values)
    if len(sorted_list) <= 1:
        return None
    else:
        return sorted_list[(len(values) - 2)]
#if value[1] then print


print(find_second_largest([1, 5, 5, 8]))
print(find_second_largest([1]))
