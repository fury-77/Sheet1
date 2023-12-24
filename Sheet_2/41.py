numbers = input("Enter a set of numbers separated by spaces: ")

numbers_str = numbers.split()
numbers = [float(number) for number in numbers_str]

sum_of_numbers = sum(numbers)

average = sum_of_numbers / len(numbers)

print("The average of the numbers is:", average)