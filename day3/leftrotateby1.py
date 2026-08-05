n = int(input("Enter size of array: "))
ar = list(map(int, input("Enter array elements: ").split()))

temp = ar[0]

for i in range(0, n - 1):
    ar[i] = ar[i + 1]

ar[n - 1] = temp

print(ar)