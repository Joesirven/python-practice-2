# Complete the sum_of_squares function which accepts
# a list of numerical values and returns the sum of
# each item squared
#
# If the list of values is empty, the function should
# return None
#
# Examples:
#   * [] returns None
#   * [1, 2, 3] returns 1*1+2*2+3*3=14
#   * [-1, 0, 1] returns (-1)*(-1)+0*0+1*1=2
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def sum_of_squares(values):
    # pass
#iterates through each and squares the variables
    sq_list = []
    if values:
        for num in values:
            sq_list.append((num ** num))
        return sum(sq_list)
    else:
        return None
#appends to a new list

#sum the list

print(sum_of_squares([1, 2, 3, 4]))
print(sum_of_squares([]))
print(sum_of_squares([-1, 0, 1]))
