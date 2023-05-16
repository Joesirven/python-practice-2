# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"

def gear_for_day(is_workday, is_sunny):
    # pass
    # empty list
    gear = []
# if not sunny and == workday, append umbrella to list
    if not is_sunny and is_workday:
        gear.append("umbrella")
# if == workday, append laptop to gear list
    if is_workday:
        gear.append("laptop")
#if not workday, append sufboard to gear list
    if not is_workday:
        gear.append("surfboard")
#if not workday, append surfboard to gear list
    if not is_workday:
        gear.append("surfboard")
    return gear

print(gear_for_day(True, False))
print(gear_for_day(False, True))
print(gear_for_day(False, False))
print(gear_for_day(True, True))
