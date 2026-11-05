def celsius_to_fahrenheit(celsius, round_to=1):
      temp = celsius * 9 / 5 + 32
     return temp
calculated_temp = celsius_to_fahrenheit(45)
print('RESULT: ', calculated_temp, "F")
print(f"Result: {calculated_temp} F")

def fahrenheit_to_celsius(fahrenheit, round_to=1):
     temp = fahrenheit - 32 * 5 / 9
     return temp
calculated_temp = fahrenheit_to_celsius(45)
print('RESULT: ', calculated_temp, "C")
print(c"Result: {calculated_temp} C")

print("\n  °C  |   °F")
print("------+-------")
for c in range(0, 101, 20):
    print(f"{c:5} | {celsius_to_fahrenheit(c):6}")

print("98.6 °F =", fahrenheit_to_celsius(98.6), "°C")
print("Round trip 37 °C:", fahrenheit_to_celsius(celsius_to_fahrenheit(37)))