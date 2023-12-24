type_list =[]
type_list_1 = int(input("plz Enter the values =>  "))
user_input_2= input("plz Enter the values =>  ")
user_input_3 = float(input("plz Enter the values =>  "))

type_1 = type_list_1,user_input_2,user_input_3

for i in type_1:
    x = type(i)
    type_list.append(x)
print(type_list)