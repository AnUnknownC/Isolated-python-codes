def cakes(recipe, available):
    a = recipe.keys()
    can = 0
    for i in a:
        if i in available:
            if can == 0:
                can = int(available[i]/recipe[i])
            if int(available[i]/recipe[i]) < can:
                can = int(available[i]/recipe[i])
        else:
            return 0
    return can

print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))
