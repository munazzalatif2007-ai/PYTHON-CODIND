choice = input("Enter shape of surface (circle, rectangle, triangle): ")
if choice == "triangle":
    base = float(input("Enter value of base of triangle:"))
    height = float(input("Enter value of height of triangle: "))
    area = (1/2) * base * height
    print("area of triangle is= " , area)
elif choice == "circle":
    radius = float(input("Enter radius of circle: "))
    area = 3.14 * radius * radius
    print("area of circle is= " , area)
elif choice == "rectangle":
    length = float(input("Enter length of rectangle:"))
    width = float(input("Enter width of rectangle:"))
    area = length * width
    print("area of rectangle is= " , area)    
else:
    print("SHAPE IS INVALID")     