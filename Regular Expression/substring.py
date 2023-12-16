import re

string = 'abc 12\
de 23 \n f45 6'
pattern = '\s+'

replace = ""
new_string = re.sub(pattern, replace, string)
print(new_string)

new_string = re.subn(pattern, replace, string)
print(new_string)
