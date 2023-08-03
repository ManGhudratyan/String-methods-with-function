def isalnum_logic(s):
    for char in s:
        if not (char.isalpha() or char.isdigit()):
            return False;
    return True;

print(isalnum_logic("Hello2023"));
print(isalnum_logic("Hello 2023"));
