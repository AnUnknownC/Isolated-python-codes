def unique_in_order(sequence):
    array = []
    a = ""
    for i in range (0, len(sequence)):
        if i == 0:
            a = sequence[i]
            array.append(sequence[i])
        else:
            if sequence[i] != a:
                a = sequence[i]
                array.append(sequence[i])
    return array

print(unique_in_order("ABBCcA"))
