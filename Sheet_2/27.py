side_1 = int(input("Enter side one => "))
side_2 = int(input("Enter side tow => "))
side_3 = int(input("Enter side three => "))


if side_1 == side_2 == side_3:
    print("Equilateral triangle")
    
elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:

    print("Isosceles triangle")
else:
    print("Scalene triangle")