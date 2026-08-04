array = [30,2,18,17,31,54]
even_count = 0
odd_count = 0
for num in array:
    if num % 2 ==0:
        even_count +=1
    else :
        odd_count +=1
print('Even count:', even_count)
print('Odd count:', odd_count)