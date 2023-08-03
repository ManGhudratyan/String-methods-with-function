def find_logic(mstr, letter):
    if type(mstr) != str:
        print('Only string.');
        return None;
    tmp = "";
    for i in range(len(mstr)):
        if mstr[i] == letter:
            tmp += str(i);
    if (tmp):
        return tmp;
    else:
        return None;
print(find_logic('Hello World', 'r'))