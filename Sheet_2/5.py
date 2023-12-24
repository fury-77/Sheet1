even_list = []
odd_list = []

numbers = [1, 2, 3, 4, 5, 6, 7, 8 ,9]

for i in numbers:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(f"Number of even numbers {len(odd_list)}")
print(f"Number of odd numbers {len(even_list)}")