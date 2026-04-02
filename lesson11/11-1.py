class Person:
    species = "human"
    count_created = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age 
        Person.count_created += 1

p1 = Person("Kelvin", 27)
p2 = Person("Madison", 24)

p1.species = "alien"

print(Person.species) # human
print(p1.species) # instance attribute alien
print(p2.species) # human

Person.species = "robot"
print(p1.species)
print(p2.species)
print(Person.species)