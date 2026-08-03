arr = [10, 7, 3, 12, 15]
target = 8

floor = max([x for x in arr if x <= target], default=None)
ceil = min([x for x in arr if x >= target], default=None)

print("Floor =", floor)
print("Ceil =", ceil)