
def replace_char(s):
    if not (s):
        return s

    first_char=s[0]
    modified_string=first_char+s[1:].replace(first_char,'$')
    return modified_string

string=input("Enter the string: ")
print(replace_char(string))

