def dig_pow(n, p):
    sum = 0
    mp = 0
    check = 0
    for i in range(0, len(str(n))):
        sum = sum + int(str(n)[i])**(i + p)
    while check < sum:
        mp += 1
        check = n * mp
    if check == sum:
        return mp
    else:
        return -1
            
print(dig_pow(114,3))
