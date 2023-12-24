my_tuple = (1, 2, 3, 2, 4, 5, 6, 6, 7)

seen = set()
repeated_items = set()

for item in my_tuple:
    if item in seen:
        repeated_items.add(item)
    else:
        seen.add(item)

if repeated_items:
    print(f"Repeated items in the tuple: {repeated_items}")
else:
    print("No repeated items found")
