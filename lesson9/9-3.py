def add_all(*args):
    total = 0
    for n in args:
        total = total + n
    return total

print(add_all(1,2,3,4,5,6,7))
print(add_all(100))
print(add_all())

def print_profile(**kwargs):
    for key in kwargs:
        print(key, "=", kwargs[key])

print_profile(name="Kelvin", city="Boston", role="Student")