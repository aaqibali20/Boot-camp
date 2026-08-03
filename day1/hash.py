arr = [1, 2, 2, 3, 1, 4, 2]

hash = {}

for i in arr:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

print(hash)
