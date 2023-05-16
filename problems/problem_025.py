# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#

def calculate_sum(values):
    # pass
# # sum(values)
#     return sum(values)
# if sum then return sum
    if values:
        return sum(values)
# else return None
    else:
        return None
print(calculate_sum([]))
print(calculate_sum([0, 12, 13, 15, 10]))
