def solution(number):
    sum = 0
    for i in range(number):
        if i%3 == 0:
            sum = sum + i
        if i%5 == 0:
            sum = sum + i
        if i%3 == 0 and i%5 == 0:
            sum = sum - i
    return sum
    pass
  
print(solution(20))
