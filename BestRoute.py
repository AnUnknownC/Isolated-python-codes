def choose_best_sum(t, k, ls):
    sum = 0
    men = 9999
    posac = 1
    for i in range(len(ls)):
        sum += ls[i]
        if posac == 4:
            posac = 0
            if men > sum:
                men = sum
            print(sum)
            sum = 0
        posac += 1

choose_best_sum(230, 4, [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89])