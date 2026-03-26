class Person:
    def __init__(self, name, age):
        print("Creating a Person Object")
        self.name = name
        self.age = age
    
    def introduce(self):
        print("Hi, my name is", self.name, "and I am", self.age)

    def birthday(self):
        self.age = self.age + 1

p1 = Person("Kelvin", 30)
p1.introduce()

p1.birthday()
p1.introduce()