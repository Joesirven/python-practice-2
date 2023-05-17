# Complete the reverse_dictionary function which has a
# single parameter that is a dictionary. Return a new
# dictionary that has the original dictionary's values
# for its keys, and the original dictionary's keys for
# its values.
#
# Examples:
#   * input:  {}
#     output: {}
#   * input:  {"key": "value"}
#     output: {"value", "key"}
#   * input:  {"one": 1, "two": 2, "three": 3}
#     output: {1: "one", 2: "two", 3: "three"}

# def reverse_dictionary(dictionary):
#     keys_list = []
#     values_list = []
#     rev_dict = {}
# # create list of keys
#     for key in dictionary:
#         keys_list.append(key)
# #create list of values
#     for value in dictionary:
#         values_list.append(value)

# #build new dictionary with key and values by matching according to the index
#     for k in keys_list:
#         rev_dict = {k : values_list[index(k)]}

#     return rev_dict

def reverse_dictionary(dictionary):
    rev_dict = {}
# create list of keys
    for k, v in dictionary.items():
        rev_dict[v] = k
    return rev_dict
#build new dictionary with key and values by matching according to the index


print(reverse_dictionary({"key": "value"}))
print(reverse_dictionary({"one": 1, "two": 2, "three": 3}))
print(reverse_dictionary({}))
