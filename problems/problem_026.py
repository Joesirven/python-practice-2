# Complete the calculate_grade function which accepts
# a list of numerical scores each between 0 and 100.
#
# Based on the average of the scores, the function
# returns
#   * An "A" for an average greater than or equal to 90
#   * A "B" for an average greater than or equal to 80
#     and less than 90
#   * A "C" for an average greater than or equal to 70
#     and less than 80
#   * A "D" for an average greater than or equal to 60
#     and less than 70
#   * An "F" for any other average

def calculate_grade(values):
    # pass
# get avg from values
    avg = sum(values)/len(values)
    print(avg)
#if avg is >= 90 return A
    if avg >= 90:
        return "A"
#elif avg is >= 80 return B
    elif avg >= 80:
        return "B"
#elif avg is >=70 return C
    elif avg >= 70:
        return "C"
#elif avg is >= 60 return D
    elif avg >= 60:
        return "D"
#else return f
    else:
        return "F"

print(calculate_grade([70, 75, 72]))
print(calculate_grade([80, 81, 82]))
print(calculate_grade([90, 92, 95]))
