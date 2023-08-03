def replace_logic(mstr, old_char, new_char):
    change_letter = "";
    
    for el in mstr:
        if el == old_char:
            change_letter += new_char;
        else:
            change_letter += el;
    return change_letter;
    
print(replace_logic('Hello World', 'l', 'k'))