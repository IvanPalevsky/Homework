strings = ["  apple ", " banana", "cherry  "]
result = list(map(lambda s: s.strip().upper(), strings))

print(result)

