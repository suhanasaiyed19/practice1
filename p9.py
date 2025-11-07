#write a python program to find the sum of even numbers using command line arguement.
import math

while True:
    print("\nMenu:")
    print("1. Find area of Circle")
    print("2. Find area of Triangle")
    print("3. Find area of Square")
    print("4. Find area of Rectangle")
    print("5. Find Simple Interest")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        radius = float(input("Enter radius of circle: "))
        area = math.pi * radius * radius
        print("Area of Circle =", area)

    elif choice == 2:
        base = float(input("Enter base of triangle: "))
        height = float(input("Enter height of triangle: "))
        area = 0.5 * base * height
        print("Area of Triangle =", area)

    elif choice == 3:
        side = float(input("Enter side of square: "))
        area = side * side
        print("Area of Square =", area)

    elif choice == 4:
        length = float(input("Enter length of rectangle: "))
        width = float(input("Enter width of rectangle: "))
        area = length * width
        print("Area of Rectangle =", area)

    elif choice == 5:
        p = float(input("Enter Principal amount: "))
        r = float(input("Enter Rate of Interest: "))
        t = float(input("Enter Time (in years): "))
        si = (p * r * t) / 100
        print("Simple Interest =", si)

    elif choice == 6:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
