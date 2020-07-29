# 2. - Accept a String input
# - Accept a String of valid chars
# - Remove all the characters that are not present in the valid chars from the input string
# - Print the cleansed String and the count of characters removed
#
# Eg. If the String input is
# I am a 5** programmer
# and the valid chars is abcdefghijklmnopqrstuvwxyz 123
# then the output should be as below
# I am a programmer
# 2 * was removed
# 1 5 was removed

str=input("Enter input string: ").lower()
final_str=str
# create list to store removed characters from str which are not present in valid char
removed_char=[]
valid_chars=input("Enter valid characters: ").lower()
for char in str:
    if(char not in valid_chars):
        # add removed char to removed_char
        removed_char.append(char)
        # delete character not present in valid char
        final_str=final_str.replace(char,'')
print("cleansed String is: ",final_str.capitalize())
# print the number of particular character removed
for i in removed_char:
     count=removed_char.count(i)
     if(count>0):
        removed_char=list(filter(lambda a: a != i, removed_char))
        print(count,i,"was removed")
