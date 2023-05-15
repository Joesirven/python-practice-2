# Complete the max_of_three function so that returns the
# maximum of three values.
#
# If two values are the same maximum value, return either of
# them.
# If the all of the values are the same, return any of them
#
# Use the >= operator for greater than or equal to

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def max_of_three(value1, value2, value3):
    pass
# turn values into integers
    value1 = int(value1)
    value2 = int(value2)
    value3 = int(value3)
# use max function to return maximum value
    # max_value = max(value1, value2, value3)
    # return max_value
    max_value = 0
# if value1 is greater than or equal to value2 and value3 make it the max value
    if value1 >= value2 and value1 >= value3:
        max_value = value1
# if value2 is greater than or equal to value1 and value3 make it the max value
    if value2 >= value1 and value2 >= value3:
        max_value = value2
# if value3 is greater than or equal to value1 and value2 make it the max value
    if value3 >= value1 and value3 >= value2:
        max_value = value3
# print(max_of_three(6, 2, 3))
    return max_value
print(max_of_three(6, 2, 3))
