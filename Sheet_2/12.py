year = int(input("Please enter a year => "))

if year > 365: 
    print(f"{year} is a leap year")
elif year <= 365:
    print(f"{year} is not a leap year")
else:
    print(f"invalid input")