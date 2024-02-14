def to_camel_case(text):
    con = ""
    may = False
    for i in text:
        if i.isalnum():
            if may:
                con += i.capitalize()
                may = False
            else:
                con += i
        else:
            may = True
    return con
        
print(to_camel_case("the-stealth-warrior"))