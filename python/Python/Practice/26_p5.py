
def dec1(func):
    def inner(*args):
        return func(*args).upper()
    return inner
def dec2(func):
    def inner(*args):
        return "<"+func(*args)+">"
    return inner
@dec2
@dec1
def changeWord(word):
    return word
str1 = "sismas u anisa i peps m u amixus f sara u mpas"
words = str1.split()
tuple1 = (changeWord(word) if word == 'u' else word for word in words)
print(' ' .join(list(tuple1)))
