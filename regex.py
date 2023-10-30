import re

txt = "the is rain in spani"

x = re.search("^the.*spani$",txt)

if x:
    print("we found a match")
else:
    print("no match")