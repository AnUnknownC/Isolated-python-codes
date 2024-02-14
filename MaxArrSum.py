def max_sequence(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        print(sum)
    if sum < 0:
        return 0
    return sum
    pass

print("v", max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))