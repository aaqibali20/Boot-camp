arr = [10, 9, 7, 4]
n = len(arr)
suffix = [0] * n

suffix[n - 1] = arr[n - 1]

for i in range(n - 2, -1, -1):
    suffix[i] = arr[i] + suffix[i + 1]
print(suffix)