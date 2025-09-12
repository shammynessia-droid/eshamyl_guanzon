def rectangle(length, width):
    area = length * width
    return area

length = float(input("Enter length: "))
width = float(input("Enter width: "))

print("Area of Rectangle:", rectangle(length, width))
