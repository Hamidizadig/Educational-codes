# import datetime
# from tokenize import String
# print(dir(datetime))
# print (vars(datetime))
# print(dir(String))
# print(datetime.__doc__)
# print(datetime.__file__)
# print(datetime.__name__)
# print(datetime.__cached__)
# help(print)
# help(datetime.datetime.now)
# help(int)

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.punctuation)
# print(string.printable)
# str1=string.capwords('rtfgh rftgh rcvgh fgh fvg fgh gh gh uik iko lij hg fg ')
# print(str1)

import string

template1 = string.Template("amswer is : $x >$y")
str1 = template1.substitute(x=23, y=14)
print(str1)
