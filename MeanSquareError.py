def solution(array_a, array_b):
    sum = 0
    arrR = []
    for i in range(len(array_a)):
        sum += (array_a[i] - array_b[i])**2
    sum = sum/len(array_a)
    return sum

def solution2(array_a, array_b):
    return sum((x - y)**2 for x, y in zip(array_a, array_b))/len(array_a)

print(solution2([1, 2, 3], [4, 5, 6]))