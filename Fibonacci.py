def productFib(prod):
    fib = [0,1]
    TF = [0]
    i = 2
    while(TF[0] < prod):   
        fib.append(fib[i-1] + fib[i-2])
        TF[0] = fib[i-1] * fib[i]
        i +=1
    TF[0] = fib[i-2]
    TF.append(fib[i-1])
    TF.append(bool(TF[0] * TF[1] == prod))
    return TF

print(productFib(5895))