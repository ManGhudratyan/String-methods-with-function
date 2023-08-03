def str_len(mstr):
    if type(mstr) != str:
        print('Write only string')
        return None;
    count = 0;
    for i in mstr:
        count += 1;
    return count;

print(str_len("Hello World"))