def is_valid_walk(walk):
    if len(walk) == 10:
        if walk.count('n') - walk.count('s') == 0 and walk.count('w') - walk.count('e')== 0:
            return True
        else:
            return False
    else:
        return False

is_valid_walk(['e', 'w', 's', 'w', 'n', 's', 'n', 's', 'e', 'w'])
#print (len(['n','s','n','s','n','s','n','s','n','s']))
#print(len(['w','e','w','e','w','e','w','e','w','e','w','e']))

['n','n','n','s','n','s','n','s','n','s']
['n','s','n','s','n','s','n','s','n','s']
