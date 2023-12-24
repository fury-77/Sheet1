user_input = int(input("Enter the price => "))
if user_input > 10000:
    x = user_input * 20//100
    print(f"the prince is {user_input}")
    print("the discount => ", int(x))

elif user_input > 7000 and user_input <= 10000:
    x = user_input * 15//100
    print(f"the price is {user_input}")
    print(f"the discount => ", int(x))

    
elif user_input <= 7000:
    x = user_input * 15//100
    print(f"the price is {user_input}")
    print(f"the discount => ", int(x))