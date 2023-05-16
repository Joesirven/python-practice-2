# Complete the remove_duplicate_letters that takes a string
# parameter "s" and returns a string with all of the
# duplicates removed.
#
# Examples:
#   * For "abc", the result is "abc"
#   * For "abcabc", the result is "abc"
#   * For "abccba", the result is "abc"
#   * For "abccbad", the result is "abcd"
#
# If the list is empty, then return the empty string.

def remove_duplicate_letters(s):
    # pass
    list = []
#iterate through string, check if in list
    for letter in s:
        if letter not in list:
            list.append(letter)
#if not in list, add to list
    for i in range(0, len(list)):
        return(list[i], end="")

#return new list

remove_duplicate_letters("abc")
remove_duplicate_letters("abcabc")
remove_duplicate_letters("abc")
