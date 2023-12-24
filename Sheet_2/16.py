number = input("Enter a number: ")

if number.isdigit() and len(number) == 3:
    print(f"{number} is a three-digit number.")
else:
    print(f"{number} is not a three-digit number.")
