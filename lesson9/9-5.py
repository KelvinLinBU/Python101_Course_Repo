def add_item(items, new_item):
    items.append(new_item)

names = ["Kelvin", "Ava"]
add_item(names," Noah")
print(names)

def add_one(x):
    x = x+1
    return x

n = 10
add_one(n)
print(n)

n = add_one(n)
print(n)