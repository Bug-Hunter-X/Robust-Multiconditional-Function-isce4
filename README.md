# ZeroDivisionError in Function with Multiple Conditions

This repository demonstrates an uncommon error in Python. The `function_with_uncommon_error` does not explicitly handle the case where both inputs are 0, causing a `ZeroDivisionError`. This example highlights the importance of comprehensive error handling, especially when dealing with multiple conditions and potential division by zero.

## Bug Description

The function uses `elif` to check for conditions, but fails to account for both `a` and `b` being 0 simultaneously. When both are 0, a `ZeroDivisionError` occurs because it attempts division by zero in the `else` block. 

## Bug Solution

The solution in `bugSolution.py` adds an explicit check for `a == 0 and b == 0` at the beginning of the function.  This prevents the `ZeroDivisionError` and provides a more robust solution.