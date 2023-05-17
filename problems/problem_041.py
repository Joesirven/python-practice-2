# Complete the add_csv_lines function which accepts a list
# as its only parameter. Each item in the list is a
# comma-separated string of numbers. The function should
# return a new list with each entry being the corresponding
# sum of the numbers in the comma-separated string.
#
# These kinds of strings are called CSV strings, or comma-
# sepearted values strings.
#
# Examples:
#   * input:  []
#     output: []
#   * input:  c
#     output: [3, 10]
#   * input:  ["8,1,7", "10,10,10", "1,2,3"]
#     output:  [16, 30, 6]
#
# Look up the string split function to find out how to
# split a string into pieces.

# Write out your own pseudocode to help guide you.

def add_csv_lines(csv_lines):
    #create a list
    sum_list = []
    #for loop spliting the string using .split
    for i in csv_lines:
        part1 = i.split(",")
        line_sum = 0
        for part in part1:
            value = int(part)
            line_sum += value
        sum_list.append(line_sum)
    #new variable
        #for loop with sum
        #append to result list
    #return result list
    return sum_list

print(add_csv_lines(["3", "10"]))
print(add_csv_lines(["8,1,7", "10,10,10", "1,2,3"]))
