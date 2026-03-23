def clamp(value, low, high):
    """
    Keep value within the inclusive range [low, high]

    If value is below low, return low
    If value is above high, return high
    Otherwise return value
    """
    if value < low:
         return low
    if value > high:
         return high
    return value 

print(clamp(5,0, 10))
print(clamp(-2, 0, 10))
print(clamp(99, 0, 10))

help(clamp)