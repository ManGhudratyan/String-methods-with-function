def isLower(mstr):
    if type(mstr) != str:
        print('Write only string.');
        return None;
    for letter in mstr:
        if not 'a' <= letter <= 'z':
            return False;
    return True;

print(isLower('hello'));
print(isLower('HELLO'))