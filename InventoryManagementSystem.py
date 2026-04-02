total_cost = []
items = [
    ["apple", "Rs.20", 50],
    ["bread", "Rs.10", 200],
    ["milk", "Rs.50", 100],
    ["eggs", "Rs.15", 1200]
]
item_name = []
item_quantity = []
item_price = []

def buy_item(index, q):
    stock_quantity = items[index][2]
    if stock_quantity >= q:
        price = items[index][1].replace("Rs.", "")
        stock_price = int(price)
        total = q * stock_price
        items[index][2] = stock_quantity - q
        total_cost.append(total)
        item_price.append(stock_price)
        item_name.append(items[index][0])
        item_quantity.append(q)
    else:
        print("Not enough stock available")

print("Welcome to our general store")
while True:
    name = input("Enter product name: ")

  
    quantity = int(input("Enter quantity of the product: "))

    if name.lower() == "apple":
        buy_item(0, quantity)
    elif name.lower() == "bread":
        buy_item(1, quantity)
    elif name.lower() == "milk":
        buy_item(2, quantity)
    elif name.lower() == "eggs":
        buy_item(3, quantity)
    else:
        print("Product not available")

    option = input("Do you want to continue (Yes/No): ")
    if option.lower() == "no":
        break

total = 0
for each in total_cost:
    total += each
vat = total * 0.13
grand_total = total + vat

print("\n============= Inventory =============")
print("{:<12} {:<12} {:<12} {:<12}".format("Item", "Qty", "Price", "Total"))
print("--------------------------------------")
for i in range(len(item_name)):
    print("{:<12} {:<12} {:<12} {:<12}".format(item_name[i], item_quantity[i], item_price[i], total_cost[i]))
print("--------------------------------------")
print("Sub total : Rs.{:.2f}".format(total))
print("VAT (13%) : Rs.{:.2f}".format(vat))
print("Total     : Rs.{:.2f}".format(grand_total))
