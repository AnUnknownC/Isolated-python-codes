def check(number):
    if len(str(number)) == 1:
        return str("0" + str(number))
    return str(number)

def make_readable(seconds):
    if seconds < 60:
        return "00:00:" + check(seconds)
    if seconds < 3599:
        return "00:" + check(int(seconds/60)) + ":" + check(seconds%60)
    return check(int(seconds/3600))+":"+check(int((seconds%3600)/60))+":"+check(int((seconds%3600)%60))
    
print(check(22))