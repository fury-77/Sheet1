myList_1 = [1, 2, 3 , 3, 4, 5, 5, 6,]

myList_2 = []

for i in myList_1:
    
    if i not in myList_2:

        myList_2.append(i)

print(myList_2)