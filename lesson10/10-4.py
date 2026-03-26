class Person:
    def __init__(self, name, age):
        print("Creating a Person Object")
        self.name = name
        self.age = age
    
    def introduce(self):
        print("Hi, my name is", self.name, "and I am", self.age)

    def birthday(self):
        self.age = self.age + 1

people = [
Person("Kelvin", 30),
Person("John", 60),
Person("Ava", 25)
]

for person in people:
    person.introduce()

for person in people:
    person.birthday()

for person in people:
    person.introduce()