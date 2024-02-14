def get_participants(handshakes):
    hs = []
    farmers = [1]
    a = 2
    if handshakes == 0:
        return 0
    while(handshakes > len(hs)):
        hs = []
        #for x, y in zip(farmers, farmers)
        for i in range(len(farmers)):
            for x in range(i + 1, len(farmers)):
                hs.append([i, x])
        if len(hs) < handshakes:
            farmers.append(a)
            a += 1
    print(farmers)
    return len(farmers)

get_participants(7)