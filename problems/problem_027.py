# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#

def max_in_list(values):
    # pass
    if values:
        return max(values)
    else:
        return None

print(max_in_list([0, 1, 3,]))
print(max_in_list([]))
print(max_in_list([1, 1, 1]))
