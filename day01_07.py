def fahrenheit_converter(c):
    f = c * 9 / 5 + 32
    return str(f) + '˚F'

c2f = fahrenheit_converter(35)

print(c2f)