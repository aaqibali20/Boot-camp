n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))

temp = arr[n - 1]   

for i in range(n - 1, 0, -1):
    arr[i] = arr[i - 1]   

arr[0] = temp   

print("Array after right rotation:", arr)