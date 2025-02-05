
def get_last_part_before_char(s,char):
    index=s.rfind(char)
    if index==-1:
        return s
    return s[:index]

string=input("Enter the string: ")
char=input("Enter the character split before: ")


print("Output: ",get_last_part_before_char(string,char))
