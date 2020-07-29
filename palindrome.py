# 1. Write a program to find out if a string is a palindrome. The string may contain spaces as well as special characters. The program should ignore the special characters and determine whether the string is a palindrome or not.
# (For example the string can be “m ad..am”. In this case the string should be read as “madam” which is a palindrome.)
import re
str=input("Enter string: ")
format_str ="".join(re.split("[^a-zA-Z]*", str))
revesed_str = format_str [::-1]
if(format_str==revesed_str):
    print("string" ,format_str,"is palindrome")
else:
    print("string" ,format_str,"is not palindrome")
