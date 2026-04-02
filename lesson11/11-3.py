class Person:
    species = "human"

    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def __str__(self):
        return f"{self.name} ({self.age})"
    
    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age})"
    
    def birthday(self): # instance
        self.age += 1

    @classmethod # class
    def from_birth_year(cls, name, birth_year, current_year):
        age = current_year - birth_year
        return cls(name, age)
    
    @staticmethod # static
    def is_adult(age):
        return age >= 18
    
p = Person("Kelvin", 27)
p.birthday()
print(p.age)

p2 = Person.from_birth_year("Madison", 2005, 2026)
print(p2.name, p2.age)

print(Person.is_adult(17))
print(Person.is_adult(21))

