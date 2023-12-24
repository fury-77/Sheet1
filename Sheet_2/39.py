even_and_odd_number = [10, 23, 24, 35, 65, 78, 90]

even_numbers = []
odd_numbers = []
for i in even_and_odd_number:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print(f"Even numbers: {even_numbers} odd numbers: {odd_numbers}")