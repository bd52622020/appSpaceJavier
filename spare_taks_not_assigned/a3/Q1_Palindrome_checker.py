#Write a Python function that checks whether a passed string is palindrome or not.

print("Welcome to palindrome checker");
string = input("Introduce your string: ");

string_list = list(string)
string_reverse = string_list[::-1]

if "".join(string_list) == "".join(string_reverse):
    print("These strings are palindromes")
else:
    print("These string are NOT palindromes")


