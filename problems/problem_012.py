# Complete the fizzbuzz function to return
# * The word "fizzbuzz" if number is evenly divisible by
#   by both 3 and 5
# * The word "fizz" if number is evenly divisible by only
#   3
# * The word "buzz" if number is evenly divisible by only
#   5
# * The number if it is not evenly divisible by 3 nor 5
#
# Try to combine what you have done in the last two problems
# from memory.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def fizzbuzz(number):
# if number % 3 == 0 and number % 5 == o return fixxbuzz
    if number % 3 == 0 and number % 5 == 0:
        return "fizzbuzz"
#elif return fizz if number % 3 == 0
    elif number % 3 == 0:
        return "fizz"
#elif return buzz if number % 5 == 0
    elif number % 5 == 0:
        return "buzz"
#else return number
    else:
        return number

print(fizzbuzz(15)) #fizzbuzz
print(fizzbuzz(3)) #fizz
print(fizzbuzz(5)) #buzz
print(fizzbuzz(4)) #4
