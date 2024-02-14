def it(a, arr):
    if a > 255: a = 255
    if a < 0:
        return arr.append(str(0)), arr.append(str(0))
    arr.append(str(deciToHexa(int(a/16)))), arr.append(str(deciToHexa(int(((a/16)%1)*16))))
    return arr

def deciToHexa(deci):
    hexa = {10 : 'A',11 : 'B',12 : 'C',13 : 'D',14 : 'E',15 : 'F'}
    if deci > 9:
        return hexa[deci]
    else:
        return deci
        
def rgb(r, g, b):
    a = ''
    arr = []
    it(r, arr),it(g, arr),it(b, arr)
    for i in range(0, len(arr)):
        a = a + arr[i]
    print(a)
    return a

rgb(-20, 275, 125)