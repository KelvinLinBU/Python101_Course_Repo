def make_min_length_checker(min_length):
    def check(text):
        return len(text) >= min_length
    return check

is_long_enough = make_min_length_checker(8)

print(is_long_enough("hello"))
print(is_long_enough("hellooooooooo"))

def normalize_names(names):
    def clean(name):
        return name.strip().lower()
    cleaned = []
    for n in names:
        cleaned.append(clean(n))
    return cleaned

raw = ["      Kelvin", "AVA", "     noah          "]
print(normalize_names(raw))
