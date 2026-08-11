arr = [3,1,8,5,2]
n = len(arr)
minIndex = 1
for i in range(0,n-2):
    for j in range(i+1,n-1):
        if arr[j] < arr[minIndex]:
            minIndex = j
    arr[i], arr[minIndex] = arr[minIndex], arr[i]
print(arr)