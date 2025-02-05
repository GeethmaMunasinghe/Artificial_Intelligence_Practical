
def first_two_chars(s1,s2):
    if len(s1)<2 or len(s2)<2:
        return "Both must have at least two characters."

    swapped_s1=s2[:2]+s1[2:]
    swapped_s2=s1[:2]+s2[2:]

    return swapped_s1+" "+swapped_s2

str1=input("Enter the first string: ")
str2=input("Enter the second string: ")

print("Output: ",first_two_chars(str1,str2))
