def likes(names):
    char = ""
    if len(names) < 4:
        if bool(names) == False:
            char = "no one likes this"
        if len(names) == 1:
            char = names[0] + " likes this"
        if len(names) > 1:
            if len(names) == 2:
                char = names[0] + " and " + names[1] + " like this"
            if len(names) == 3:
                char = names[0] + ", " + names[1] + " and " + names[2] + " like this"
    else:
        char = names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like this"
    return char

print(likes(['Alex', 'Jacob']))
