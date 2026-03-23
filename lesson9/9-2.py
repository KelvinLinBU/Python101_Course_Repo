def compute_tax_and_total(price, tax_rate = .0625):
    tax = price * tax_rate
    total = price + tax
    return tax, total

tx, tl = compute_tax_and_total(100)

print(tx)
print(tl)

tl, tx = compute_tax_and_total(100, .10)

print(tx)
print(tl)