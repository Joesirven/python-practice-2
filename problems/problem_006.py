# Complete the can_skydive function so that determines if
# someone can go skydiving based on these criteria
#
# * The person must be greater than or equal to 18 years old, or
# * The person must have a signed consent form

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def can_skydive(age, has_consent_form):
    # ask for input of name, age, consent form
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    has_consent_form = bool(input("Do you have a signed consent form? (Yes/No)"))
    # age needs to be int, has_consent_form needs to be bool
    # new variable can_skydive = False
    if age >= 18 and has_consent_form == True:
        print(f"{name}!, You can go skydiving!")
    else:
        print(f"{name}!, You're trash and cannot go skydiving.")

    # turn into if statement, age is >= 18 AND has_consent_form == true

    # if can_skydive == True: print name or you can go skydiving
    return can_skydive


can_skydive(0, False)
