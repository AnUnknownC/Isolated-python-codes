def check(poss):
    if poss[2] == 8:
        poss[len(poss)-1] = '`0`'
    print(poss[len(poss)-1])
    return poss

def get_pins(observed):
    keyboard = [['1','2','3'],
                ['4','5','6'],
                ['7','8','9'],
                ['','0','']]
    poss = [-3,-1,0,1,3]
    for i in range(len(poss)):
        poss[i] = str(int(observed) + poss[i])
    poss = check(poss)
    return poss

    # 5 = [2,4,5,6,8] 8 = [5,7,8,9,0]
    #      n-3/,n-1/,n,n+1,n+3
    

print(get_pins('8'))