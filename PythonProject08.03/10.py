def merge_dicts(d1, d2):
    result = d1.copy()
    for key, value in d2.items():

        result[key] = result.get(key, 0) + value
    return result
print(merge_dicts({"a": 1, "b": 2}, {"a": 1, "b": 2}))

