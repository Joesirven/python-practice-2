# Complete the pairwise_add function which accepts two lists
# of the same size. It creates a new list and populates it
# with the sum of corresponding entries in the two lists.
#
# Examples:
#   * list1:  [1, 2, 3, 4]
#     list2:  [4, 5, 6, 7]
#     result: [5, 7, 9, 11]
#   * list1:  [100, 200, 300]
#     list2:  [ 10,   1, 180]
#     result: [110, 201, 480]
#
# Look up the zip function to help you with this problem.

def pairwise_add(list1, list2):
    # result1 = []
    # result2 = []
    result = []
    # for i in list1:
    #     result1.append(i)
    # for b in list2:
    #     result2.append(b)
    # for r in range(len(list1)):
    #     result.append(list1[r]+list2[r])
    # return result

    #zip 2 lists together
    combined_lists = zip(list1, list2)
    #for loop adding to the touples together using sum
    for item in combined_lists:
        result.append(sum(item))
    #append to new list

    #return result
    return result

# for loop with both lists that adds them and appends to a new list
print(pairwise_add([1, 2, 3, 4], [4, 5, 6, 7]))
