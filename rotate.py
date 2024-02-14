def rotate(str_):
    lst = []
    if bool(str_) == False:
        return []
    else:
        rot = str_ + str_[0]
        for i in range(len(str_)):
            rot = rot.replace(rot[0],"",1)
            lst.append(rot)
            rot = rot + rot[0] 
        return lst

print(rotate([]))