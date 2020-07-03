import string
letters = string.ascii_lowercase + string.ascii_uppercase
x = 'January 1, 2000'
char_list = [char for char in x  if char in letters]

print(char_list)