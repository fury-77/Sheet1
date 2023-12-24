cost_price = int(input("Please enter the price => "))

if cost_price > 100000:
    print("Tax => 15%")
elif cost_price > 50000 and cost_price <= 100000:
    print("Tax => 10%")
elif cost_price <= 50000:
    print("Tax => 5%")