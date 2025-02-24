groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]

while True:
    item = input("Enter an item to remove from the list (or type 'stop' to quit): ").lower()
    
    if item == "stop":
        break
    
    if item in groceries:
        groceries.remove(item)
        print(f"{item} removed. Updated list: {groceries}")
    else:
        print(f"{item} is not in the list.")

print("Updated grocery list:", groceries)