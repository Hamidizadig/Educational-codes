class Person:
    count = 0

    def __init__(self, name, family):
        self.name = name
        self.family = family
        Person.count += 1

    def __str__(self):
        return self.name+"\t\t"+self.family

    def __del__(self):
        print(self.name+"  end")


p1 = Person("sanaz", "abbas")
print(str(p1))
print(Person.count)

p2 = Person("sasi", "izakis")
print(str(p2))
print(Person.count)

p1.name = "sasha"
print(str(p1))
print(str(p2))


del(p2)
