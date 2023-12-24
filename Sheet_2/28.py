number_1 = int(input("Enter the first number => "))
number_2 = int(input("Enter the second number => "))
operator = input("Enter the operator => ")

if operator == '*':
    print(number_1*number_2)

elif operator == '-':
    print(number_1 - number_2)

elif operator == '+':
    print(number_2 + number_2)

elif operator == '%':
    print(number_1 % number_2)

elif operator == '/':
    print(number_1 / number_1)
else:
    print("invalid operator")