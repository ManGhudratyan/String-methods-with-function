def isUpper(mstr):
    if type(mstr) != str:
        print('Write only string.');
        return None;
    for letter in mstr:
        if not 'A' <= letter <= 'Z':
            return False;
    return True;

print(isUpper('Hello'));
print(isUpper('HELLO'));

