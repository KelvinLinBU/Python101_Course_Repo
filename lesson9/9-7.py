from utility import clean_name, compute_total

raw_names = ["Kelvin", "john               "]
cleaned =[]
for n in raw_names:
    cleaned.append(clean_name(n))

print(cleaned)
print(compute_total(100))
