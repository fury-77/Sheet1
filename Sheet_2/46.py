n = int(input("Input the value for nth term: "))
running_sum = 0

for i in range(1, n + 1):
    running_sum += i
    series = '+'.join(map(str, range(1, i + 1)))
    print(f"{series} = {running_sum}")

print(f"The sum of the above series is: {running_sum}")

