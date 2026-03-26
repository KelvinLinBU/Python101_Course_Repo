class Person:
    def __init__(self, name, age):
        print("Creating a Person Object")
        self.name = name
        self.age = age

p1 = Person("Kelvin", 30)
p2 = Person("John", 60)

print(p1.name, p1.age)
print(p2.name, p2.age)