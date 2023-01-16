### Iterator
import random
piscture=['a.jpg','b.jpg','c.jpg','d.jpg','e.jpg','f.jpg','g.jpg','h.jpg','x.jpg',]
def fun1(piscture):
    return random.choice(piscture)
for p1 in iter (lambda:fun1(piscture),'e.jpg'):
    print(p1)
