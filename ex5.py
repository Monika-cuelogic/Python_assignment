a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

res = list(set(a) & set(b))
res1 = list(set(a).intersection(set(b)))

print(f"Common elements in both the lists are: {res}")
print(f"Common elements in both the lists are: {res1}")