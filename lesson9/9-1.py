def discounted_price(price, discount_percent):
    if price < 0:
        return None
    if discount_percent < 0 or discount_percent > 100:
        return None
    discount_amount = price * (discount_percent / 100)
    return price - discount_amount

print(discounted_price(100, 20)) 
print(discounted_price(50,0))
print(discounted_price(-10, 20)) #None
print(discounted_price(100,200)) #None