class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def describe(self):
        print(f"{self.name} is {self.age} years old")

    def speak(self):
        print(f"{self.name} makes a sound")

animal1 = Animal("Generic Animal", 5)

animal1.describe()
animal1.speak()

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def speak(self):
        print(f"{self.name} barks")

dog1 = Dog("Buddy", 3, "Golden Retriever")
print(dog1.name)
print(dog1.age)
print(dog1.breed)

dog1.describe()
dog1.speak()

class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, age)
        self.indoor = indoor
    
    def speak(self):
        print(f"{self.name} Meows")

cat1 = Cat("Whiskers", 1, True)
print(cat1.indoor)
cat1.describe()
cat1.speak()

