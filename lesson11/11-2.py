class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def __str__(self):
        return f"{self.name} ({self.age})"
    
    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age})"

p1 = Person("Kelvin", 27)
p2 = Person("Madison", 24)

print(p1)
print(p2)

people = [p1, p2]
print(people)

s = "Kelvin\nLin"
print(s)
print(repr(s))