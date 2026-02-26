def is_passing(score):
    return score >= 60

print(is_passing(60))
print(is_passing(59))

def safe_divide(a,b):
    if b == 0:
        print("error, divide by 0")
        return None
    return a/b

print(safe_divide(10,2))
print(safe_divide(10,0))