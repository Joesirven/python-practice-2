# Complete the can_make_pasta function to
# * Return true if the ingredients list contains
#   "flour", "eggs", and "oil"
# * Otherwise, return false
#
# The ingredients list will always contain three items.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def can_make_pasta(ingredients):
# if ingredients contain flour eggs and oil return true
    if "flour" in ingredients and "eggs" in ingredients and "oil" in ingredients:
        return True
    else:
        return False
#else return false

ingredients = ["flour", "eggs", "oil"]
print(can_make_pasta(ingredients))

ingredients = ["flour", "eggs", "salt"]
print(can_make_pasta(ingredients))
