salary = int(input("Enter your salary => "))
year = int(input("How long have you been working for the company => "))

if year > 10:
    print("You've got bonus 10%")
    x = salary * 10/100
    print(int(x))

elif year >= 6 and year <= 10:
    print("You've got bonus 8%")
    x = salary * 8/100
    print(int(x))

elif year < 6:
    print("You've got bonus 5%")
    x = salary * 5/100
    print(int(x))


