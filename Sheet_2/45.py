number = int(input("Please enter the number => "))
for i in range(1, number + 1):
    result = i * number
    print( i , '*',  i ,'=' ,i * i)
sum_result = sum(i * i for i in range (1, number + 1))
print(f"the sum result => {sum_result}")