# Complete the is_inside_bounds function which takes an x
# coordinate and a y coordinate, and then tests each to
# make sure they're between 0 and 10, inclusive.

def is_inside_bounds(x, y):
    return x >= 0 and x <= 10 and y >= 0 and y <= 10


# print(is_inside_bounds(5, 5))
# print(is_inside_bounds(11, 5))
# print(is_inside_bounds(5, 11))
# print(is_inside_bounds(11, 11))
