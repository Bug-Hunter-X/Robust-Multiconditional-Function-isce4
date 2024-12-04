def function_with_uncommon_error(a, b):
    if a == 0 and b == 0:
        return 0  # Handle the case where both a and b are 0
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_error(0,0)
print(result)