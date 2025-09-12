def km_to_miles(km):
 	return km * 0.621371
def celcius_to_fahrenheit(c):
 	return (c * 9/5) + 32

km = float(input("Enter distance in kilometers: "))
c = float(input("Enter temperature in Celsius: "))

print(f"{km} kilometers is equal to {km_to_miles(km)} miles.")
print(f"{c} degrees Celsius is equal to {celcius_to_fahrenheit(c)} degrees Fahrenheit.")