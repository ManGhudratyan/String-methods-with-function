def split_logic(mstr, symb):
    ml = [];
    tmp = "";
    for el in mstr:
        if el == symb:
            ml.append(tmp);
            tmp = "";
        else:
            tmp += el;
    if tmp:
        ml.append(tmp)
    return ml;
    
print(split_logic('Hello World', ' '));