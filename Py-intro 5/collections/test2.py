dict1 = {'a': 4, 'b': 16, 'c': 3}
dict2 = {'a': 8, 'b': 2, 'c': 3}

# Iterate over the keys in dict1, multiply the values for each key from both dicts, and sum the results
result = sum(dict1[key] * dict2[key] for key in dict1)

# Print the final result
print(result)