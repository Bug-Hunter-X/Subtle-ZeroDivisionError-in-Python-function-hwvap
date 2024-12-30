def function_with_uncommon_error_solution(a, b):
    try:
        if a == 0:
            return float('inf')  # Return infinity or handle appropriately
        return a + b
    except ZeroDivisionError as e:
        return f'Error: {e}' #Better error handling

result = function_with_uncommon_error_solution(0, 5)
print(result) #Output: inf
result2 = function_with_uncommon_error_solution(5, 0)
print(result2) # Output: 5