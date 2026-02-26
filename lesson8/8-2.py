def compute_total(price, tax_rate=.0625):
    tax = price * tax_rate
    total = price + tax
    return total

print(compute_total(100))
print(compute_total(100, 1))
print(compute_total(price=100, tax_rate=.1))

