def addGl(func):
    def inner(*args):
        return "<"+func(*args)+">"
    return inner



def addSq(func):
    def inner(*args):
        return "#"+func(*args)+"#"
    return inner

def addStar(func):
    def inner(*args):
        return "*"+func(*args)+"*"
    return inner



@addGl
@addSq
@addStar
def gettext(str1):
    return str1

print(gettext('shipsix'))