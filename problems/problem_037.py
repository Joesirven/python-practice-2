# Complete the pad_left function which takes three parameters
#   * a number
#   * the number of characters in the result
#   * a padding character
# and turns the number into a string of the desired length
# by adding the padding character to the left of it
#
# Examples:
#   * number: 10
#     length: 4
#     pad:    "*"
#     result: "**10"
#   * number: 10
#     length: 5
#     pad:    "0"
#     result: "00010"
#   * number: 1000
#     length: 3
#     pad:    "0"
#     result: "1000"
#   * number: 19
#     length: 5
#     pad:    " "
#     result: "   19"

def pad_left(number, length, pad):
    # pass
# pad_length = measure len of number, and subtract that from the length
    pad_length = (length - len(str(number)))
# padding * pad_length + str(num)
    return (pad*pad_length) + str(number)

print(pad_left(19, 5, " "))
print(pad_left(1000, 12, "0"))
