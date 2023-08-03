def strip_logic(mstr):
    for i in range(len(mstr)):
        if not mstr[i].isspace():
            break

    for j in range(len(mstr), 0, -1):
        if not mstr[j - 1].isspace():
            break

    return mstr[i:j]

print(strip_logic("   Hello, World!   "));
