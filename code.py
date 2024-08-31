print("Welcome to Taste Trek :)")

menu = {
    "pizza regular": 700,
    "piza large": 1300,
    "crispy zinger": 500,
    "cofee": 600,
    "drinks": 150,
    "broast": 800,
    "rolls": 300
}

print("Pizza Regular |   Rs.700\n"
      "Pizza Large   |   Rs.1300\n"
      "Zinger        |   Rs.500\n"
      "Coffee        |   Rs.600\n"
      "Drinks        |   Rs.150\n"
      "Broast        |   Rs.800\n"
      "Rolls         |   Rs.300")

order_total = 0
while True:
    item = input("Enter your order (or type 'exit' to finish): ").lower()
    
    if item == "exit":
        break
    
    if item in menu:
        order_total += menu[item]
        print(f"Successfully, your {item} is added to your bill!")
    else:
        print("Please order something from our menu. You entered an unlisted item.")
    
    another_order = input("Do you want to add something more (yes/no)? ").lower()
    
    if another_order == "no":
        break

print(f"Your total bill before tax is Rs.{order_total}")

# Adding tax
tax = order_total * 0.10
total_with_tax = order_total + tax
print(f"Your bill after tax addition is Rs.{total_with_tax}")
