# Write a function that takes a temperature in fahrenheit and returns the temperature in celsius.

def f_to_c(fahrenheit_input):
    celsius = ((fahrenheit_input - 32) * 5) / 9
    print(f"{celsius:.1f}")

f_to_c(32)
f_to_c(113)
f_to_c(26.6)