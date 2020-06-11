#Write a Python program to match a string that contains only upper and 
# lowercase letters, numbers, and underscores. 

import re;

text = "This text _only conta1ns all0weD chars";

reg = re.search("^([\s_a-zA-Z0-9]*)$", text)

if reg is None:
    print("Not found")
else:
    print("Found")