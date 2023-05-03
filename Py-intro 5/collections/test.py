def capitalize_long_strings(lst):
    result = []
    for item in lst:
        if len(item) >= 5:
            # result.append(item.capitalize())
            result.append(item.upper())
    return result




lst = ["apple", "banana", "cat", "dog", "elephant", "frog"]
print(capitalize_long_strings(lst)) # Output: ['APPLE', 'BANANA', 'ELEPHANT']