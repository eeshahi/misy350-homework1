inventory = [
    {"item_id": 1, "name": "Espresso", "unit_price": 2.50, "stock": 40},
    {"item_id": 2, "name": "Latte", "unit_price": 4.25, "stock": 25},
    {"item_id": 3, "name": "Cold Brew", "unit_price": 3.75, "stock": 30},
    {"item_id": 4, "name": "Mocha", "unit_price": 4.50, "stock": 20},
    {"item_id": 5, "name": "Blueberry Muffin", "unit_price": 2.95, "stock": 18},
]

Orders = [
    {"orders_id": "Order_101", "items_id":2, "Quantity": 2, "Status": "Placed", "Total": 8.50},
    {"orders_id": "Order_102", "items_id":3, "Quantity": 1, "Status": "Placed", "Total": 3.75},
]

# Query 0: View all items in the inventory with stock less than 20.

# 1. Input:
# Define the threshold for low stock (20) and access the inventory list.
threshold = 5

# 2. Process: Find items with stock below threshold
# Loop through the inventory to find matches
low_stock_items = []
for item in inventory:
    if item["stock"] < threshold:
        # Found one! Add it to our result list
        low_stock_items.append(item)

# 3. Output:
# Print the results
if len(low_stock_items) > 0:
    print("Low stock items found:")
    for item in low_stock_items:
        print(f"- {item['name']}: {item['stock']}")
else:
    print("No low stock items.")


# Query 1: Place a new order for an item and quantity.
print("--------------------------------------------")
print("Query 1")
# 1. Input:
item_id = int(input("Enter the Item ID to order: "))
quantity = int(input("Enter the quantity: "))

# 2. Process: [Name process here, e.g. "Validate and create order"]
new_quantity= None
placed = False
old_quantity = None

for item in inventory:
    if item["item_id"] == item_id:
        found = True
        old_quantity = item["stock"]
        if item["stock"] >= quantity:
            total_price = item["unit_price"] * quantity
            Orders.append( {
                "orders_id": f"Order_{len(Orders) + 101}",
                "items_id": item_id,
                "Quantity": quantity,
                "Status": "Placed",
                "Total": total_price
            })

            item["stock"] = item["stock"] - quantity
            new_quantity = item["stock"] 
            placed = True
            break

# 3. Output:
if found and placed:
    print("Order placed:")
    print("Updated stock for item_id", item_id, "reduces from", old_quantity , "to", new_quantity)
else:
    print("Not enough stock or invalid quantity")




## Query 2:** View all orders placed for a particular item — prompt the user to enter the item name.
# View all orders placed for a particular item.
# Prompt the user for the item name.
print("--------------------------------------------")
print("Query 2")
# 1. Input:
search_item = input("Enter the item name to search (e.g. 'Latte'): ")



# 2. Process: [Name process here, e.g. "Find orders for item"]
matched_item_id = None
exists = False
matched_item_id = 0   
matched_orders = []

for item in inventory:
    if item["name"] == search_item:
        exists = True
        matched_item_id = item["item_id"]
        break

if exists:
    for order in Orders:
        if order["items_id"] == matched_item_id:
            matched_orders.append(order)

# 3. Output:
if not exists:
    print("Item not found in inventory.")
else:
    print("Orders for", search_item + ":")
    for order in matched_orders:
        print("- Order ID:", order["orders_id"],
              "| Quantity:", order["Quantity"],
              "| Total:", order["Total"])
        


##Query 3:** Calculate and print the total number of orders placed for "Cold Brew".
# Query 3: Total number of orders placed for "Cold Brew".
print("--------------------------------------------")
print("Query 3")
# 1. Input:
search_item = "Cold Brew"

# 2. Process: [Name process here, e.g. "Count orders"]
matched_item_id = None
exists = False
matched_item_id = 0
order_count = 0

for item in inventory:
    if item["name"] == search_item:
        exists = True
        matched_item_id = item["item_id"]
        break
if exists:
    for order in Orders:
        if order["items_id"] == matched_item_id:
            order_count = order_count + 1


# 3. Output:
if exists:
    print("Total number of orders placed for", search_item, ":", order_count)
else:
    print("Item not found in inventory.")
 


### Update" Query 4:** Prompt the user to enter an item id and new quantity. Update the item stock quantity.
# Query 4: Update item stock quantity by item id.
print("--------------------------------------------")
print("Query 4")
# 1. Input:
item_id = int(input("Enter ID of item to update: "))
new_stock = int(input("Enter new stock quantity: "))

# 2. Process: [Name process here, e.g. "Validate and update stock"]
exists = False
old_stock = 0

for item in inventory:
    if item["item_id"] == item_id:
        exists = True
        old_stock = item["stock"]
        item["stock"] = new_stock
        break

# 3. Output:
if exists:
    print("Stock updated for item_id", item_id)
    print("Cold Brew stock updates from", old_stock, "to", new_stock, ".")
else:
    print("Item not found.")

### Remove/Delete
##Query 5:** Cancel an order (and restore stock) using the steps below:
##1. Prompt the user to enter an order ID.
##2. Find that order in the `orders` list.
##3. Change the order `status` to `Cancelled`.
##4. Read the `item_id` and `quantity` from the order.
##5. Locate the matching item in `inventory` and add the quantity back to its `stock`.

# Query 5: Cancel an order and restore stock.
print("--------------------------------------------")
print("Query 5")
# 1. Input:
cancel_order_id = input("Enter Order ID to cancel: ")


# 2. Process: [Name process here, e.g. "Cancel order"]
order_found = False
item_found = False
restore_quantity = 0
restore_item_id = 0

for order in Orders:
    if order["orders_id"] == cancel_order_id:
        order_found = True
        order["Status"] = "Cancelled"
        restore_item_id = order["items_id"]
        restore_quantity = order["Quantity"]
        break

if order_found:
    for item in inventory:
        if item["item_id"] == restore_item_id:
            item_found = True
            item["stock"] = item["stock"] + restore_quantity
            break


# 3. Output:
if order_found and item_found:
    print('Order status changes to "Cancelled", and Stock for Item', restore_item_id,"(", item["name"] + ")", "increases back by", restore_quantity)
else:
    print("Order ID not found.")

