number = int(input("Please enter a number => "))

if number == 1:
    print("Not Prime")
if number > 1:
    for i in range(2,number):
        if number % 2 == 0:
            print(f"{number} Is not a prime number")
            break
        else:
             print(f"{number} Is a prime number")
