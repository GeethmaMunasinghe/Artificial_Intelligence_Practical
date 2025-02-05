
def first_and_last_two_chars(s):
    if len(s)<2:
        return ""
    return s[:2]+string[-2:]

string=input("Enter a String: ")
print("Result: ", first_and_last_two_chars(string))
