def capitalize_logic(mstr):
    if (mstr[0].islower()):
        word = mstr[0].upper() + mstr[1:];
        return word;
    else:
        return mstr;
    
print(capitalize_logic('hello world.'));
    
    